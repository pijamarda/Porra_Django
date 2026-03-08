def build_bracket(bracket_template, slot_map, knockout_matches=None, knockout_predictions=None):
    """
    bracket_template     : Tournament.bracket_template JSON
    slot_map             : {slot_label: Team} from ClassificationEngine
    knockout_matches     : {(round_name, order): Match}
    knockout_predictions : {(round_name, order): Prediction}

    Returns {round_name: [match_dict]} where each match_dict has:
      order, home (Team|None), away (Team|None),
      match (Match|None), prediction (Prediction|None), winner (Team|None)
    """
    knockout_matches = knockout_matches or {}
    knockout_predictions = knockout_predictions or {}
    result = {}
    round_winners = {}  # 'winner_r16_1' -> Team or None

    for round_name in bracket_template['rounds']:
        result[round_name] = []
        for tmpl in bracket_template[round_name]:
            order = tmpl['order']
            home = slot_map.get(tmpl['home']) or round_winners.get(tmpl['home'])
            away = slot_map.get(tmpl['away']) or round_winners.get(tmpl['away'])
            prediction = knockout_predictions.get((round_name, order))
            match = knockout_matches.get((round_name, order))

            winner = None
            if home and away and prediction:
                if prediction.home_goals > prediction.away_goals:
                    winner = home
                elif prediction.away_goals > prediction.home_goals:
                    winner = away
                # draw → winner stays None (shows ? in next round)

            round_winners[f'winner_{round_name}_{order}'] = winner
            result[round_name].append({
                'order': order,
                'home': home,
                'away': away,
                'match': match,
                'prediction': prediction,
                'winner': winner,
            })

    return result
