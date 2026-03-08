from django.apps import AppConfig


class TournamentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tournaments'

    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth.models import User
        from .models import Match
        from .scoring import recalculate_user_ranking

        def on_match_saved(sender, instance, **kwargs):
            if instance.result_known:
                for user in User.objects.all():
                    recalculate_user_ranking(user, instance.tournament)

        post_save.connect(on_match_saved, sender=Match)
