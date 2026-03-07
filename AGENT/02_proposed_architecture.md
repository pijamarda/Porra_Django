# Proposed Architecture — Porra Django (HTMX Rewrite)

## Goals

1. **Eliminate code duplication** — one generic `tournaments` app instead of `euro2016` + `mundial2014`
2. **Replace jQuery AJAX with HTMX** — simpler, declarative, no JS file to maintain
3. **Use django-template-partials** — define named fragments inside templates, reuse them for HTMX responses without separate endpoint templates
4. **Complete the points system** — add real match results, auto-score predictions
5. **Improve security** — move secrets to environment variables

---

## New tech stack

| Layer | Technology |
|---|---|
| Framework | Django 5.2 LTS |
| Database | PostgreSQL |
| Frontend | Bootstrap 5 + HTMX 2.x |
| Partial templates | `django-template-partials` |
| JS | Minimal (only where HTMX truly can't do it) |
| Python | 3.10+ |

---

## New app structure

```
porrasite/
├── porrasite/          # Django project config
├── accounts/           # Replaces home/ — auth, registration, user profile
├── tournaments/        # Single generic tournament app (replaces euro2016 + mundial2014)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── scoring.py      # Replaces tools.py — group standings + points
│   ├── admin.py
│   └── templates/
│       └── tournaments/
│           ├── base.html
│           ├── index.html
│           ├── rank_list.html
│           ├── group_detail.html     # Group standings + match inputs (with partials)
│           ├── knockout.html         # Knockout bracket (with partials)
│           └── partials/             # Standalone HTMX response fragments (fallback)
└── static/
    └── css/porra.css   # Bootstrap 5 overrides only — no custom JS file
```

---

## New data models

### `tournaments` app

```python
class Tournament(models.Model):
    name                = models.CharField(max_length=100)   # "Euro 2016"
    slug                = models.SlugField(unique=True)      # "euro2016"
    year                = models.IntegerField()
    active              = models.BooleanField(default=False)
    classification_type = models.CharField(max_length=50)    # see ClassificationEngine below
    bracket_template    = models.JSONField()                 # see below

class Group(models.Model):
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name        = models.CharField(max_length=10)   # "A", "B"...
    order       = models.IntegerField()

class Team(models.Model):
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    group       = models.ForeignKey(Group, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    flag_code   = models.CharField(max_length=20)   # 'es', 'br'

class Match(models.Model):
    """Real match — shared for all users. Admin fills in actual results."""
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round       = models.CharField(max_length=20)   # 'group', 'r16', 'qf', 'sf', 'final'
    home_team   = models.ForeignKey(Team, null=True, related_name='home_matches')
    away_team   = models.ForeignKey(Team, null=True, related_name='away_matches')
    home_goals  = models.IntegerField(null=True, blank=True)  # actual result (admin)
    away_goals  = models.IntegerField(null=True, blank=True)
    date        = models.DateField(null=True, blank=True)
    order       = models.IntegerField()             # for bracket ordering

class Prediction(models.Model):
    """One prediction per user per match."""
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    match       = models.ForeignKey(Match, on_delete=models.CASCADE)
    home_goals  = models.IntegerField(default=0)
    away_goals  = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'match')

class UserRanking(models.Model):
    """Computed total points per user per tournament."""
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    points      = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'tournament')
```

**Key improvement:** `Match` is shared — no per-user match rows for the actual fixture. Only `Prediction` is per-user. This reduces rows from `51 × N_users` (current) to `51 + 51 × N_users`.

---

## Tournament classification system

This is the core design challenge. Each tournament has its own rules for:

1. **Group ranking** — same everywhere (W=3pts, D=1pt, L=0), tiebreakers may vary slightly
2. **Who qualifies from groups** — top 2 always yes, but what happens with third-place teams?
3. **How third-place teams are ranked** — by pts, then GD, then GF across all groups
4. **Which bracket slots third-place teams fill** — depends on *which* groups they came from (lookup table)

### Strategy pattern: `ClassificationEngine`

Each tournament declares a `classification_type` key. A registry maps keys to Python classes:

```python
# tournaments/classification.py

class ClassificationEngine:
    """Base class. Each tournament type subclasses this."""

    def rank_group(self, teams_with_stats) -> list:
        """Sort teams within a group by standard football rules."""
        # Pts → GD → GF → head-to-head — same for all tournaments
        ...

    def get_group_qualifiers(self, group_standings) -> dict:
        """Return {'winner': team, 'runner_up': team} from a group."""
        raise NotImplementedError

    def get_third_place_qualifiers(self, all_group_standings) -> list:
        """
        Return the list of qualifying third-place teams (may be empty).
        Override in tournaments that have third-place qualification.
        """
        return []

    def assign_bracket_slots(self, qualifiers, tournament) -> dict:
        """
        Given all qualifiers, return a mapping of bracket slot label → team.
        e.g. {'1A': team_spain, '2B': team_france, '3ABCD': team_italy, ...}
        The bracket_template JSON uses these labels to build matches.
        """
        raise NotImplementedError


class StandardClassification(ClassificationEngine):
    """Top 2 from each group only. No third-place. WC2014 style."""

    def get_group_qualifiers(self, standings):
        return {'winner': standings[0], 'runner_up': standings[1]}

    def assign_bracket_slots(self, qualifiers, tournament):
        slots = {}
        for group_name, q in qualifiers.items():
            slots[f'1{group_name}'] = q['winner']
            slots[f'2{group_name}'] = q['runner_up']
        return slots


class EuroThirdPlaceClassification(ClassificationEngine):
    """Top 2 + 4 best third-place teams. Euro 2016 style."""

    N_THIRD_PLACE = 4

    # Which bracket slots third-place teams fill depends on which 4 groups
    # they came from. This lookup table is fixed by UEFA.
    THIRD_PLACE_SLOT_MAP = {
        frozenset('ABCD'): {'A': '3D', 'B': '3E', 'C': '3F', 'D': '3A/B/C'},
        frozenset('ABCE'): {'A': '3D', 'B': '3E', 'C': '3F', 'E': '3A/B/C'},
        # ... all 15 combinations of 4 groups from 6
    }

    def get_third_place_qualifiers(self, all_group_standings):
        thirds = [s[2] for s in all_group_standings.values()]  # 3rd of each group
        thirds.sort(key=lambda t: (-t.pts, -t.gd, -t.gf))
        return thirds[:self.N_THIRD_PLACE]

    def assign_bracket_slots(self, qualifiers, tournament):
        slots = {}
        for group_name, q in qualifiers['groups'].items():
            slots[f'1{group_name}'] = q['winner']
            slots[f'2{group_name}'] = q['runner_up']
        # Third-place slot labels depend on which groups qualified
        third_groups = frozenset(t.group.name for t in qualifiers['thirds'])
        slot_labels = self.THIRD_PLACE_SLOT_MAP[third_groups]
        for group_name, slot_label in slot_labels.items():
            team = next(t for t in qualifiers['thirds'] if t.group.name == group_name)
            slots[slot_label] = team
        return slots


# Registry — add new engines here without touching anything else
ENGINES = {
    'standard':           StandardClassification,
    'euro_third_place':   EuroThirdPlaceClassification,
    # 'wc2026':           WC2026Classification,  # add when needed
}

def get_engine(tournament) -> ClassificationEngine:
    return ENGINES[tournament.classification_type]()
```

### `bracket_template` JSON field

The knockout bracket structure is stored as JSON on the `Tournament`, using slot labels:

```json
{
  "rounds": ["r16", "qf", "sf", "final"],
  "r16": [
    {"order": 1, "home": "1A", "away": "2C"},
    {"order": 2, "home": "1B", "away": "3A/D/E/F"},
    {"order": 3, "home": "1C", "away": "3A/B/C"},
    ...
  ],
  "qf": [
    {"order": 1, "home": "winner_r16_1", "away": "winner_r16_2"},
    ...
  ]
}
```

This JSON is loaded once as a fixture per tournament. When computing a user's bracket view, `ClassificationEngine.assign_bracket_slots()` fills in the actual teams, and the bracket template defines the match structure. Adding WC2026 means writing a new JSON fixture and (if the third-place rule is new) a new engine subclass — no model changes.

### How it all fits together

```
compute_user_bracket(user, tournament):
    engine = get_engine(tournament)
    group_standings = {g: engine.rank_group(predictions) for g in groups}
    third_qualifiers = engine.get_third_place_qualifiers(group_standings)
    slot_map = engine.assign_bracket_slots({
        'groups': group_standings,
        'thirds': third_qualifiers
    }, tournament)
    # Use bracket_template + slot_map to build the knockout view
    return build_bracket(tournament.bracket_template, slot_map)
```

This replaces the current `tools.py` in each app. New tournament = new fixture + optionally new engine class.

---

## Compute on GET, write only on POST

### The current problem

The current `actualizar_grupo` function mixes two unrelated things:

1. **Computation** — calculates group standings (pts, W, D, L, GD, GF) from match predictions
2. **Persistence** — writes the derived bracket state back to the DB (e.g. sets `partido_id=40.local_id = winner_of_group_A`)

This means **every page load writes to the database**. The `eliminatorias` view makes it worse — it calls `actualizar_eliminatorias` four times in sequence just to cascade results through knockout rounds. A single page visit triggers dozens of DB writes as a side effect of a read.

This is wrong for three reasons:
- **Semantics**: GET requests should be read-only and idempotent
- **Performance**: unnecessary DB writes on every visit
- **Correctness**: if two users load the page simultaneously they can corrupt each other's data

### The new approach: pure computation on GET

In the new architecture, **bracket state is never stored in the database**. It is always computed fresh from the user's predictions:

```
GET /euro2016/knockout/

view:
  predictions = Prediction.objects.filter(user=user, match__tournament=tournament)
  engine      = get_engine(tournament)
  standings   = engine.rank_group(predictions)   # pure Python, no DB writes
  slot_map    = engine.assign_bracket_slots(...)  # pure Python, no DB writes
  bracket     = build_bracket(tournament.bracket_template, slot_map)
  return render(template, {bracket: bracket})

POST /euro2016/predictions/<match_id>/save/

view:
  prediction.home_goals = request.POST['home_goals']
  prediction.away_goals = request.POST['away_goals']
  prediction.save()                               # one DB write, nothing else
  return render(partial_template, {prediction: prediction})
```

The cascade through knockout rounds (octavos → cuartos → semis → final) happens entirely in Python during rendering, with zero DB writes. The bracket template JSON defines the cascade structure; `build_bracket` follows it in a single pass.

### Why this is fast enough

The computation per page load:
- Fetch `N` predictions for one user (one DB query with a filter)
- Sort 4 teams per group in Python (trivial)
- Walk the bracket template JSON (linear traversal)

For Euro 2016: 51 predictions fetched, 6 groups computed, bracket walked once. This is sub-millisecond in Python. No caching needed at this scale.

### Caching (if the app grows)

If the number of users grows significantly, the group standings for a given user only change when that user saves a prediction. Django's per-view cache or a simple `cache.set(f'standings:{user_id}:{tournament_id}', data)` call in the prediction save view would be enough — invalidated on every POST, served instantly on every GET.

---

## Points system (complete)

Defined in `tournaments/scoring.py`:

```python
def score_prediction(prediction: Prediction) -> int:
    """
    Rules (suggested — adjust to taste):
      - Exact score:           3 points
      - Correct result (W/D/L) + correct goal difference: 2 points
      - Correct result only:   1 point
      - Wrong:                 0 points
    """

def recalculate_user_ranking(user, tournament):
    """Re-scores all predictions for finished matches, updates UserRanking."""
```

Admin enters real results on `Match`. A Django signal on `Match.save()` triggers `recalculate_user_ranking` for all users.

---

## URL structure

```
/<slug>/                          → tournament index        [tournament:index]
/<slug>/ranking/                  → global ranking          [tournament:ranking]
/<slug>/groups/                   → all groups overview     [tournament:groups]
/<slug>/groups/<group_id>/        → group detail + matches  [tournament:group_detail]
/<slug>/knockout/                 → knockout bracket        [tournament:knockout]
/<slug>/predictions/<user_id>/    → another user's view     [tournament:user_predictions]

# HTMX endpoints (return partial HTML, not full pages)
/<slug>/predictions/<match_id>/edit/   → inline edit form   [tournament:prediction_edit]
/<slug>/predictions/<match_id>/save/   → POST, returns updated row [tournament:prediction_save]
```

No more separate `/edita_partido_ajax/`, `/list_partido_ajax/`, `/suma_puntos/` — HTMX handles this with standard URLs returning HTML fragments.

---

## HTMX interaction pattern

### Inline score editing (replaces jQuery AJAX)

**Template fragment inside `group_detail.html`:**

```html
{% load partials %}

{% partialdef match_row inline=True %}
<tr id="match-{{ prediction.pk }}">
  <td>{{ prediction.match.home_team.name }}</td>
  <td>
    <form hx-post="{% url 'tournament:prediction_save' slug match.pk %}"
          hx-target="#match-{{ prediction.pk }}"
          hx-swap="outerHTML">
      {% csrf_token %}
      <input type="number" name="home_goals" value="{{ prediction.home_goals }}"
             min="0" max="20" style="width:3rem"
             hx-trigger="change" hx-include="closest form">
      -
      <input type="number" name="away_goals" value="{{ prediction.away_goals }}"
             min="0" max="20" style="width:3rem"
             hx-trigger="change" hx-include="closest form">
    </form>
  </td>
  <td>{{ prediction.match.away_team.name }}</td>
</tr>
{% endpartialdef %}
```

**View:**

```python
def prediction_save(request, slug, match_pk):
    # Save prediction
    prediction.home_goals = request.POST['home_goals']
    prediction.away_goals = request.POST['away_goals']
    prediction.save()
    # Return only the updated row — no full page reload
    return TemplateResponse(request, 'tournaments/group_detail.html#match_row',
                            {'prediction': prediction, 'match': prediction.match})
```

The `#match_row` fragment selector is provided by `django-template-partials`. The view returns only that `<tr>` snippet. HTMX swaps it into the DOM. Zero custom JavaScript.

### Group standings auto-refresh

```html
<div id="group-{{ group.pk }}-standings"
     hx-get="{% url 'tournament:group_standings' slug group.pk %}"
     hx-trigger="every 30s">
  {% include "tournaments/partials/group_standings.html" %}
</div>
```

After any prediction save, HTMX can also trigger a standings refresh via `hx-trigger="save-prediction from:body"` and a custom event dispatched by the save response header:

```python
response['HX-Trigger'] = 'save-prediction'
```

---

## Migration plan

### Step 1 — New `tournaments` app alongside existing apps
- Create models, load Euro 2016 and Mundial 2014 data via fixtures or management command
- Keep `euro2016` and `mundial2014` apps running — no disruption

### Step 2 — Migrate user data
- Write a migration script: for each user, convert their `PartidoEuro2016` rows → `Prediction` rows linked to the new `Match` objects

### Step 3 — Build new templates with HTMX
- Add `django-template-partials` and `htmx` to the project
- Build new templates feature by feature, verifiable against old ones

### Step 4 — Switch routing
- Update `porrasite/urls.py` to route to new `tournaments` views
- Keep old URLs as redirects during transition

### Step 5 — Remove old apps
- Delete `euro2016/`, `mundial2014/`
- Remove signal-based Partido/Rank creation

---

## Dependencies to add

```
# requirements.txt additions
django-template-partials==24.4   # Named template fragments for HTMX
whitenoise==6.9.0                # Serve static files without Nginx in dev/simple prod
```

HTMX itself is loaded from CDN or as a static file — no npm needed:

```html
<script src="https://unpkg.com/htmx.org@2.0.4"></script>
```

---

## Security improvements (separate from HTMX work)

Add to `settings.py`:

```python
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
```

Add to `.env`:

```
DJANGO_SECRET_KEY=<generate with python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())">
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## What stays the same

- Bootstrap (upgrade 3 → 5)
- Country flag PNGs in `static/img/`
- Django admin for entering real match results
- Docker Compose setup
- PostgreSQL

---

## Implementation order (recommended)

1. `settings.py` security fixes (30 min, zero risk)
2. New `tournaments` models + admin (1–2 hours)
3. Load fixture data into new models (1 hour)
4. Build group detail view + HTMX inline editing (2–3 hours) — this is the core
5. Build knockout bracket view with HTMX (2–3 hours)
6. Implement points scoring system (2 hours)
7. Rankings view (1 hour)
8. Migrate user predictions from old models (1–2 hours)
9. Remove old apps (1 hour)
