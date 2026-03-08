from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

from .bracket import build_bracket
from .classification import get_engine
from .models import Group, Match, Prediction, Tournament, UserRanking


def tournament_list(request):
    tournaments = Tournament.objects.all().order_by('-year')
    return TemplateResponse(request, 'tournaments/tournament_list.html', {
        'tournaments': tournaments,
    })


def _get_predictions(user, matches):
    """Return {match_id: Prediction}, creating missing ones with defaults."""
    existing = {
        p.match_id: p
        for p in Prediction.objects.filter(user=user, match__in=matches)
    }
    to_create = [
        Prediction(user=user, match=m, home_goals=0, away_goals=0)
        for m in matches
        if m.id not in existing
    ]
    if to_create:
        Prediction.objects.bulk_create(to_create)
        existing.update({p.match_id: p for p in to_create})
    return existing


def ranking(request, slug):
    tournament = get_object_or_404(Tournament, slug=slug)
    rankings = UserRanking.objects.filter(tournament=tournament).select_related('user').order_by('-points')
    return TemplateResponse(request, 'tournaments/ranking.html', {
        'tournament': tournament,
        'rankings': rankings,
    })


def tournament_index(request, slug):
    tournament = get_object_or_404(Tournament, slug=slug)
    groups = tournament.groups.prefetch_related('teams')
    ranking = UserRanking.objects.filter(tournament=tournament).select_related('user')
    return TemplateResponse(request, 'tournaments/index.html', {
        'tournament': tournament,
        'groups': groups,
        'ranking': ranking,
    })


def _get_third_place_qualifies(request, tournament, group, group_predictions):
    """Return True if this group's 3rd-place team qualifies based on current predictions."""
    engine = get_engine(tournament)
    if not hasattr(engine, 'get_third_place_qualifiers'):
        return None  # not applicable for this tournament type
    groups = list(tournament.groups.prefetch_related('teams'))
    all_group_matches = list(
        Match.objects.filter(tournament=tournament, round=Match.ROUND_GROUP)
        .select_related('home_team', 'away_team', 'group')
    )
    all_predictions = _get_predictions(request.user, all_group_matches)
    all_predictions.update(group_predictions)
    all_standings = {g.name: engine.rank_group(g, all_predictions) for g in groups}
    third_qualifiers = engine.get_third_place_qualifiers(all_standings)
    qualifying_team_ids = {s.team.id for s in third_qualifiers}
    group_standings = all_standings[group.name]
    if len(group_standings) < 3:
        return None
    return group_standings[2].team.id in qualifying_team_ids


@login_required
def group_detail(request, slug, group_id):
    tournament = get_object_or_404(Tournament, slug=slug)
    group = get_object_or_404(Group, tournament=tournament, pk=group_id)
    groups = tournament.groups.all()
    matches = list(group.matches.select_related('home_team', 'away_team').order_by('order'))

    predictions = _get_predictions(request.user, matches)
    engine = get_engine(tournament)
    standings = engine.rank_group(group, predictions)
    match_predictions = [(m, predictions.get(m.id)) for m in matches]
    third_place_qualifies = _get_third_place_qualifies(request, tournament, group, predictions)

    return TemplateResponse(request, 'tournaments/group_detail.html', {
        'tournament': tournament,
        'group': group,
        'groups': groups,
        'match_predictions': match_predictions,
        'standings': standings,
        'active_group_pk': group.pk,
        'third_place_qualifies': third_place_qualifies,
        'predictions_open': tournament.predictions_open,
    })


@login_required
def knockout(request, slug):
    tournament = get_object_or_404(Tournament, slug=slug)
    bracket_rounds = _compute_knockout_context(request, tournament)
    return TemplateResponse(request, 'tournaments/knockout.html', {
        'tournament': tournament,
        'bracket_rounds': bracket_rounds,
        'predictions_open': tournament.predictions_open,
    })


@login_required
@require_POST
def knockout_prediction_save(request, slug, match_id):
    tournament = get_object_or_404(Tournament, slug=slug)
    if not tournament.predictions_open:
        return HttpResponseForbidden('Predictions are closed.')
    match = get_object_or_404(Match, tournament=tournament, pk=match_id)

    pred, _ = Prediction.objects.get_or_create(
        user=request.user, match=match,
        defaults={'home_goals': 0, 'away_goals': 0},
    )
    try:
        pred.home_goals = max(0, int(request.POST.get('home_goals', 0)))
        pred.away_goals = max(0, int(request.POST.get('away_goals', 0)))
    except (ValueError, TypeError):
        pass
    pred.save()

    bracket_rounds = _compute_knockout_context(request, tournament)
    return TemplateResponse(request, 'tournaments/knockout.html#knockout_content', {
        'tournament': tournament,
        'bracket_rounds': bracket_rounds,
        'predictions_open': tournament.predictions_open,
    })


def _compute_knockout_context(request, tournament):
    """Shared helper: computes full bracket context for knockout view and save."""
    groups = list(tournament.groups.prefetch_related('teams'))
    group_matches = list(
        Match.objects.filter(tournament=tournament, round=Match.ROUND_GROUP)
        .select_related('home_team', 'away_team', 'group')
    )
    predictions = _get_predictions(request.user, group_matches)
    engine = get_engine(tournament)
    group_standings = {g.name: engine.rank_group(g, predictions) for g in groups}
    group_qualifiers = {
        name: engine.get_group_qualifiers(standings)
        for name, standings in group_standings.items()
    }
    third_qualifiers = engine.get_third_place_qualifiers(group_standings)
    slot_map = engine.assign_bracket_slots(
        {'groups': group_qualifiers, 'thirds': third_qualifiers},
        tournament,
    )
    knockout_match_list = list(
        Match.objects.filter(tournament=tournament).exclude(round=Match.ROUND_GROUP)
    )
    knockout_matches = {(m.round, m.order): m for m in knockout_match_list}
    knockout_preds = _get_predictions(request.user, knockout_match_list)
    knockout_predictions = {
        (m.round, m.order): knockout_preds[m.id]
        for m in knockout_match_list
        if m.id in knockout_preds
    }
    bracket = build_bracket(
        tournament.bracket_template, slot_map,
        knockout_matches=knockout_matches,
        knockout_predictions=knockout_predictions,
    )
    round_labels = {'r16': 'Round of 16', 'qf': 'Quarter-finals', 'sf': 'Semi-finals', 'final': 'Final'}
    return [
        {'name': r, 'label': round_labels.get(r, r), 'matches': bracket[r]}
        for r in tournament.bracket_template.get('rounds', [])
    ]


@login_required
@require_POST
def prediction_save(request, slug, match_id):
    tournament = get_object_or_404(Tournament, slug=slug)
    if not tournament.predictions_open:
        return HttpResponseForbidden('Predictions are closed.')
    match = get_object_or_404(Match, tournament=tournament, pk=match_id)

    pred, _ = Prediction.objects.get_or_create(
        user=request.user, match=match,
        defaults={'home_goals': 0, 'away_goals': 0},
    )
    try:
        pred.home_goals = max(0, int(request.POST.get('home_goals', 0)))
        pred.away_goals = max(0, int(request.POST.get('away_goals', 0)))
    except (ValueError, TypeError):
        pass
    pred.save()

    # Recompute standings so the partial response is up to date
    group = match.group
    matches = list(group.matches.select_related('home_team', 'away_team').order_by('order'))
    predictions = _get_predictions(request.user, matches)
    engine = get_engine(tournament)
    standings = engine.rank_group(group, predictions)
    match_predictions = [(m, predictions.get(m.id)) for m in matches]
    third_place_qualifies = _get_third_place_qualifies(request, tournament, group, predictions)

    # Return only the group content partial — HTMX swaps it in place
    return TemplateResponse(request, 'tournaments/group_detail.html#group_content', {
        'tournament': tournament,
        'group': group,
        'match_predictions': match_predictions,
        'standings': standings,
        'third_place_qualifies': third_place_qualifies,
        'predictions_open': tournament.predictions_open,
    })
