from django.contrib import admin

from .models import Tournament, Group, Team, Match, Prediction, UserRanking


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'slug', 'classification_type', 'active', 'predictions_locked', 'predictions_deadline']
    list_editable = ['predictions_locked']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'year', 'active', 'classification_type', 'bracket_template']}),
        ('Prediction locking', {'fields': ['predictions_deadline', 'predictions_locked'],
                                'description': 'Set a deadline for automatic locking, or use the manual override.'}),
    ]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'name', 'order']
    list_filter = ['tournament']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament', 'group', 'flag_code']
    list_filter = ['tournament', 'group']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'round', 'order', 'home_team', 'away_team', 'home_goals', 'away_goals', 'date']
    list_filter = ['tournament', 'round']
    list_editable = ['home_goals', 'away_goals']  # admin can enter real results inline


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'match', 'home_goals', 'away_goals']
    list_filter = ['match__tournament', 'user']


@admin.register(UserRanking)
class UserRankingAdmin(admin.ModelAdmin):
    list_display = ['user', 'tournament', 'points']
    list_filter = ['tournament']
    ordering = ['tournament', '-points']
