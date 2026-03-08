from .models import Prediction, UserRanking


def score_prediction(prediction):
    """
    Exact score:                    3 points
    Correct result + correct GD:    2 points
    Correct result only:            1 point
    Wrong:                          0 points
    """
    match = prediction.match
    if not match.result_known:
        return 0

    ph, pa = prediction.home_goals, prediction.away_goals
    rh, ra = match.home_goals, match.away_goals

    def outcome(h, a):
        if h > a:
            return 'W'
        if h < a:
            return 'L'
        return 'D'

    if ph == rh and pa == ra:
        return 3
    if outcome(ph, pa) == outcome(rh, ra):
        if (ph - pa) == (rh - ra):
            return 2
        return 1
    return 0


def recalculate_user_ranking(user, tournament):
    predictions = Prediction.objects.filter(
        user=user,
        match__tournament=tournament,
        match__home_goals__isnull=False,
        match__away_goals__isnull=False,
    ).select_related('match')

    total = sum(score_prediction(p) for p in predictions)
    UserRanking.objects.update_or_create(
        user=user,
        tournament=tournament,
        defaults={'points': total},
    )
