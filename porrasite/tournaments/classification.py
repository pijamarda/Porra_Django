from dataclasses import dataclass, field


@dataclass
class TeamStats:
    team: object  # Team model instance
    played: int = 0
    won: int = 0
    drawn: int = 0
    lost: int = 0
    gf: int = 0   # goals for
    ga: int = 0   # goals against

    @property
    def gd(self):
        return self.gf - self.ga

    @property
    def pts(self):
        return self.won * 3 + self.drawn


class ClassificationEngine:

    def rank_group(self, group, predictions_by_match_id):
        """
        Given a Group and a dict of {match_id: Prediction},
        return a list of TeamStats sorted by standings (pts desc, gd desc, gf desc).
        """
        teams = list(group.teams.all())
        team_ids = {t.id for t in teams}
        stats = {t.id: TeamStats(team=t) for t in teams}

        for match in group.matches.select_related('home_team', 'away_team'):
            pred = predictions_by_match_id.get(match.id)
            if pred is None:
                continue
            if match.home_team_id not in team_ids or match.away_team_id not in team_ids:
                continue

            home = stats[match.home_team_id]
            away = stats[match.away_team_id]
            hg, ag = pred.home_goals, pred.away_goals

            home.gf += hg; home.ga += ag; home.played += 1
            away.gf += ag; away.ga += hg; away.played += 1

            if hg > ag:
                home.won += 1; away.lost += 1
            elif hg < ag:
                away.won += 1; home.lost += 1
            else:
                home.drawn += 1; away.drawn += 1

        return sorted(
            stats.values(),
            key=lambda s: (-s.pts, -s.gd, -s.gf, s.team.name),
        )

    def get_group_qualifiers(self, standings):
        return {'winner': standings[0], 'runner_up': standings[1]}

    def get_third_place_qualifiers(self, all_standings):
        return []

    def assign_bracket_slots(self, qualifiers, tournament):
        slots = {}
        for group_name, q in qualifiers['groups'].items():
            slots[f'1{group_name}'] = q['winner'].team
            slots[f'2{group_name}'] = q['runner_up'].team
        return slots


class StandardClassification(ClassificationEngine):
    """Top 2 from each group. No third-place qualifiers. WC2014 style."""
    pass


class EuroThirdPlaceClassification(ClassificationEngine):
    """Top 2 + best 4 third-place teams. Euro 2016 style."""

    N_THIRD_PLACE = 4

    # UEFA fixed lookup: given which 4 groups produced qualifying third-place teams,
    # which R16 slot does each one fill?
    # Slot labels mean: '3A' = third-place team that plays vs Winner A in R16,
    #                   '3B' = third-place team that plays vs Winner B in R16, etc.
    # Derived from Euro 2016 draw rules (tools.py source of truth).
    THIRD_PLACE_SLOT_MAP = {
        frozenset(['A','B','C','D']): {'A':'3C',  'B':'3D',  'C':'3A',  'D':'3B'},
        frozenset(['A','B','C','E']): {'A':'3B',  'B':'3C',  'C':'3A',  'E':'3D'},
        frozenset(['A','B','C','F']): {'A':'3B',  'B':'3C',  'C':'3A',  'F':'3D'},
        frozenset(['A','B','D','E']): {'A':'3B',  'B':'3C',  'D':'3A',  'E':'3D'},
        frozenset(['A','B','D','F']): {'A':'3B',  'B':'3C',  'D':'3A',  'F':'3D'},
        frozenset(['A','B','E','F']): {'A':'3B',  'B':'3C',  'E':'3A',  'F':'3D'},
        frozenset(['A','C','D','E']): {'A':'3C',  'C':'3A',  'D':'3B',  'E':'3D'},
        frozenset(['A','C','D','F']): {'A':'3C',  'C':'3A',  'D':'3B',  'F':'3D'},
        frozenset(['A','C','E','F']): {'A':'3B',  'C':'3A',  'E':'3D',  'F':'3C'},
        frozenset(['A','D','E','F']): {'A':'3B',  'D':'3A',  'E':'3D',  'F':'3C'},
        frozenset(['B','C','D','E']): {'B':'3C',  'C':'3A',  'D':'3B',  'E':'3D'},
        frozenset(['B','C','D','F']): {'B':'3C',  'C':'3A',  'D':'3B',  'F':'3D'},
        frozenset(['B','C','E','F']): {'B':'3C',  'C':'3B',  'E':'3A',  'F':'3D'},
        frozenset(['B','D','E','F']): {'B':'3C',  'D':'3B',  'E':'3A',  'F':'3D'},
        frozenset(['C','D','E','F']): {'C':'3A',  'D':'3B',  'E':'3D',  'F':'3C'},
    }

    def get_third_place_qualifiers(self, all_standings):
        thirds = [s[2] for s in all_standings.values()]
        thirds.sort(key=lambda s: (-s.pts, -s.gd, -s.gf))
        return thirds[:self.N_THIRD_PLACE]

    def assign_bracket_slots(self, qualifiers, tournament):
        slots = super().assign_bracket_slots(qualifiers, tournament)
        third_groups = frozenset(s.team.group.name for s in qualifiers['thirds'])
        slot_labels = self.THIRD_PLACE_SLOT_MAP.get(third_groups, {})
        for group_name, slot_label in slot_labels.items():
            team_stats = next(
                s for s in qualifiers['thirds']
                if s.team.group.name == group_name
            )
            slots[slot_label] = team_stats.team
        return slots


ENGINES = {
    'standard':         StandardClassification,
    'euro_third_place': EuroThirdPlaceClassification,
}


def get_engine(tournament):
    engine_class = ENGINES.get(tournament.classification_type, StandardClassification)
    return engine_class()
