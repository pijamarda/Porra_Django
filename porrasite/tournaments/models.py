from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tournament(models.Model):
    name                 = models.CharField(max_length=100)
    slug                 = models.SlugField(unique=True)
    year                 = models.IntegerField()
    active               = models.BooleanField(default=False)
    classification_type  = models.CharField(max_length=50)
    bracket_template     = models.JSONField(default=dict)
    predictions_deadline = models.DateTimeField(
        null=True, blank=True,
        help_text='Predictions automatically close after this date/time (UTC).',
    )
    predictions_locked   = models.BooleanField(
        default=False,
        help_text='Manual override: lock predictions regardless of deadline.',
    )

    @property
    def predictions_open(self):
        if self.predictions_locked:
            return False
        if self.predictions_deadline and timezone.now() > self.predictions_deadline:
            return False
        return True

    def __str__(self):
        return self.name


class Group(models.Model):
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='groups')
    name        = models.CharField(max_length=10)  # "A", "B", ...
    order       = models.IntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ('tournament', 'name')

    def __str__(self):
        return f'{self.tournament.slug} — Group {self.name}'


class Team(models.Model):
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')
    group       = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='teams')
    name        = models.CharField(max_length=100)
    flag_code   = models.CharField(max_length=20)

    class Meta:
        ordering = ['group__order', 'name']

    def __str__(self):
        return f'{self.name} ({self.tournament.slug})'


class Match(models.Model):
    ROUND_GROUP = 'group'
    ROUND_R32   = 'r32'
    ROUND_R16   = 'r16'
    ROUND_QF    = 'qf'
    ROUND_SF    = 'sf'
    ROUND_FINAL = 'final'
    ROUND_CHOICES = [
        (ROUND_GROUP, 'Group stage'),
        (ROUND_R32,   'Round of 32'),
        (ROUND_R16,   'Round of 16'),
        (ROUND_QF,    'Quarter-final'),
        (ROUND_SF,    'Semi-final'),
        (ROUND_FINAL, 'Final'),
    ]

    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    group       = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name='matches')
    round       = models.CharField(max_length=10, choices=ROUND_CHOICES)
    order       = models.IntegerField()             # global ordering within tournament
    home_team   = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='home_matches')
    away_team   = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='away_matches')
    home_goals  = models.IntegerField(null=True, blank=True)  # actual result — filled by admin
    away_goals  = models.IntegerField(null=True, blank=True)
    date        = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        home = self.home_team.name if self.home_team else '?'
        away = self.away_team.name if self.away_team else '?'
        return f'{self.tournament.slug} {self.round}: {home} vs {away}'

    @property
    def result_known(self):
        return self.home_goals is not None and self.away_goals is not None


class Prediction(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')
    match       = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='predictions')
    home_goals  = models.IntegerField(default=0)
    away_goals  = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'match')

    def __str__(self):
        return f'{self.user.username}: {self.match} → {self.home_goals}-{self.away_goals}'


class UserRanking(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rankings')
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='rankings')
    points      = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'tournament')
        ordering = ['-points']

    def __str__(self):
        return f'{self.user.username} — {self.tournament.slug}: {self.points}pts'
