import random

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User, Group
from .models import Rank, Partido

#Este metodo se invoca cuando se genera un usuario y lo que hace es generar todos los partidos del usuario
#Genera 64 partidos en principio con un resultado aleatorio
#Esta variable marcara si queremos el resultado aleatorio
# = 1 Indica que no es aleatorio y todos los resultados son 0 - 0
# = n indica un resultado variable entre 0 y n-1
RESULTADO_DEFAULT = 4

@receiver(post_save, sender=User)
def init_new_user(instance, created, raw, **kwargs):
	# raw is set when model is created from loaddata.
	if (created and not raw):
		#instance.groups.add(Group.objects.get(name='new-user-group'))
		print("usuario creado")
		Rank.objects.create(usuario=instance, puntos=0)

		#GRUPO A
		Partido.objects.create(usuario=instance, partido_id=1, local_id=1, visitante_id=2, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=2, local_id=3, visitante_id=4, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=17, local_id=1, visitante_id=3, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=18, local_id=4, visitante_id=2, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=33, local_id=4, visitante_id=1, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=34, local_id=2, visitante_id=3, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO B
		Partido.objects.create(usuario=instance, partido_id=3, local_id=5, visitante_id=6, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=4, local_id=7, visitante_id=8, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=19, local_id=5, visitante_id=7, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=20, local_id=8, visitante_id=6, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=35, local_id=8, visitante_id=5, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=36, local_id=6, visitante_id=7, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO C
		Partido.objects.create(usuario=instance, partido_id=5, local_id=9, visitante_id=10, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=6, local_id=11, visitante_id=12, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=21, local_id=9, visitante_id=11, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=22, local_id=12, visitante_id=10, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=37, local_id=12, visitante_id=9, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=38, local_id=10, visitante_id=11, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO D
		Partido.objects.create(usuario=instance, partido_id=7, local_id=13, visitante_id=14, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=8, local_id=15, visitante_id=16, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=23, local_id=13, visitante_id=15, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=24, local_id=16, visitante_id=14, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=39, local_id=16, visitante_id=13, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		Partido.objects.create(usuario=instance, partido_id=40, local_id=14, visitante_id=15, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))

        