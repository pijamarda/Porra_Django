import random

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User, Group
from .models import Rank, Partido

@receiver(post_save, sender=User)
def init_new_user(instance, created, raw, **kwargs):
    # raw is set when model is created from loaddata.
    if (created and not raw):
        #instance.groups.add(Group.objects.get(name='new-user-group'))
        print("usuario creado")
        Rank.objects.create(usuario=instance, puntos=0)

        for i in range(1,65):
            Partido.objects.create(usuario=instance, partido_id=i, local_id=random.randrange(1,32), visitante_id=random.randrange(1,32), local=random.randrange(5), visitante=random.randrange(5))

        