# Current Architecture — Porra Django

## What the app does

A football tournament prediction game ("porra"). Before a competition starts, users fill in predicted scores for every match. Once the tournament runs, they earn points based on how accurate their predictions were. Currently supports Euro 2016 and World Cup 2014.

---

## Tech stack

| Layer | Technology |
|---|---|
| Framework | Django 5.2 |
| Database | PostgreSQL (via docker-compose), SQLite locally |
| Frontend | Bootstrap 3 + jQuery 2.2.4 |
| AJAX | Custom jQuery handlers → Django JSON/HTML endpoints |
| Deployment | uWSGI + Nginx (legacy), Docker Compose (current) |
| Python | 3.10.12 |

---

## Project layout

```
porrasite/
├── porrasite/          # Django project config (settings, root urls, wsgi)
├── home/               # Auth: login, register, home page
├── euro2016/           # Euro 2016 tournament (self-contained app)
├── mundial2014/        # World Cup 2014 tournament (self-contained app)
├── static/
│   ├── js/mundial-ajax.js   # jQuery AJAX handlers
│   ├── css/mundial.css
│   └── img/                 # 250+ country flag PNGs
└── manage.py
```

---

## Data models

### Per tournament (duplicated in euro2016 and mundial2014)

```
Grupo           → Tournament group (A, B, C...)
Equipo          → Team (belongs to a Grupo, has flag code)
Partido*        → One match prediction per user
                  (local_id, visitante_id, local_goals, visitante_goals)
Rank*           → One ranking record per user
                  (puntos + one int field per group for qualification points)
```

`*` The Partido and Rank models are per-user records. Each time a user registers, signals auto-create:
- One Rank record (0 points)
- N Partido records (51 for Euro2016, 64 for Mundial2014) — scores randomised 0-3

### User
Django's built-in `auth.User`. No profile model.

---

## URL structure

```
/                         → home
/accounts/                → login, logout, register
/euro2016/                → tournament index
/euro2016/rank/           → global rankings
/euro2016/user/<pk>/      → user's match list
/euro2016/user/<pk>/grupo/<gid>/        → group standings
/euro2016/user/<pk>/eliminatorias/      → knockout list
/euro2016/user/<pk>/eliminatorias/tabla → knockout bracket
/euro2016/edita_partido_ajax/           → AJAX POST: update one match
/euro2016/list_partido_ajax/            → AJAX GET: list match IDs
/euro2016/suma_puntos/                  → AJAX GET: recalculate points
/mundial2014/             → mirrors same structure
```

---

## Business logic

All tournament logic lives in `tools.py` in each app:

- **`actualizar_grupo(grupo_id, user)`** — computes group standings from all predicted match results (W/D/L, goal difference, goals for). Determines which 2 teams qualify.
- **`actualizar_grupo_3rd(user)`** — (Euro only) determines which 4 best third-place teams also qualify.
- **`actualizar_eliminatorias(user)`** — propagates qualifiers through Round of 16 → Quarters → Semis → Final by reading the predicted group standings.
- **`get_partidos_fase_grupos(grupo_id, user)`** — returns the 6 matches in a group for a given user.

---

## Frontend interaction flow

1. User visits `/euro2016/user/<pk>/grupo/<gid>/`
2. Page shows group table + 6 match score inputs
3. User edits a score → jQuery clicks `.euro2016_edit_ajax`
4. jQuery POSTs to `/euro2016/edita_partido_ajax/` with `{partido_id, local, visitante}`
5. Django saves the Partido, recalculates standings, returns an HTML snippet
6. jQuery replaces a `<div>` on the page

The knockout bracket (`eliminatorias_tabla.html`) is a complex static HTML table with `<input>` fields — it has partial AJAX support via `.list_partido_ajax`.

---

## What is incomplete / broken

| Area | Issue |
|---|---|
| Points system | `suma_puntos` view exists but the scoring rules are not fully implemented. `RankEuro2016.puntos` is never automatically updated when real results come in. |
| Admin input of real results | There is no model or view for admins to enter the *actual* match results. The `Partido` model stores only user predictions; real results would need a separate model. |
| Mundial2014 | Largely a copy-paste of euro2016, some views are missing or incomplete (e.g. 3rd place logic differs). |
| jQuery AJAX | Only group stage editing is wired up properly. Knockout bracket editing is partial. |
| Security | `SECRET_KEY` is hardcoded in settings.py. `DEBUG=True` is hardcoded. |
| No generic tournament model | Adding a new tournament (Euro 2024, World Cup 2026) requires duplicating the entire app. |

---

## Key files

| File | Purpose |
|---|---|
| [porrasite/settings.py](../porrasite/porrasite/settings.py) | Django config |
| [euro2016/models.py](../porrasite/euro2016/models.py) | Core data models |
| [euro2016/tools.py](../porrasite/euro2016/tools.py) | Tournament business logic |
| [euro2016/views.py](../porrasite/euro2016/views.py) | Views + AJAX endpoints |
| [euro2016/signals.py](../porrasite/euro2016/signals.py) | Auto-create user data on registration |
| [static/js/mundial-ajax.js](../porrasite/static/js/mundial-ajax.js) | jQuery AJAX handlers |
| [home/templates/home/base.html](../porrasite/home/templates/home/base.html) | Base template |
