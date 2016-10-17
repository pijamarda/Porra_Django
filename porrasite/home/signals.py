import random

from django.db.models.signals import post_save
from django.dispatch import receiver


from euro2016.models import RankEuro2016, PartidoEuro2016
from django.contrib.auth.models import User, Group

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
		#RankEuro2016.objects.create(usuario=instance, puntos=0, a1=0, a2=0, b1=0, b2=0)
		RankEuro2016.objects.create(usuario=instance)

		#GRUPO A
		PartidoEuro2016.objects.create(usuario=instance, partido_id=1, local_id=1, visitante_id=2, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=2, local_id=3, visitante_id=4, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=14, local_id=2, visitante_id=4, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=15, local_id=1, visitante_id=3, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=25, local_id=2, visitante_id=3, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=26, local_id=4, visitante_id=1, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO B
		PartidoEuro2016.objects.create(usuario=instance, partido_id=3, local_id=7, visitante_id=8, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=4, local_id=5, visitante_id=6, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=13, local_id=6, visitante_id=8, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=16, local_id=5, visitante_id=7, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=27, local_id=6, visitante_id=7, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=28, local_id=8, visitante_id=5, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO C
		PartidoEuro2016.objects.create(usuario=instance, partido_id=6, local_id=11, visitante_id=12, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=7, local_id=9, visitante_id=10, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=17, local_id=10, visitante_id=12, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=18, local_id=9, visitante_id=11, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=29, local_id=10, visitante_id=11, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=30, local_id=12, visitante_id=9, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO D
		PartidoEuro2016.objects.create(usuario=instance, partido_id=5, local_id=15, visitante_id=16, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=8, local_id=13, visitante_id=14, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=20, local_id=14, visitante_id=16, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=21, local_id=13, visitante_id=15, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=31, local_id=14, visitante_id=15, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=32, local_id=16, visitante_id=13, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO E
		PartidoEuro2016.objects.create(usuario=instance, partido_id=9, local_id=19, visitante_id=20, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=10, local_id=17, visitante_id=18, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=19, local_id=18, visitante_id=20, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=22, local_id=17, visitante_id=19, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=35, local_id=18, visitante_id=19, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=36, local_id=20, visitante_id=17, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#GRUPO F
		PartidoEuro2016.objects.create(usuario=instance, partido_id=11, local_id=23, visitante_id=24, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=12, local_id=21, visitante_id=22, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=23, local_id=22, visitante_id=24, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=24, local_id=21, visitante_id=23, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=33, local_id=22, visitante_id=23, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=34, local_id=24, visitante_id=21, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))		

		#Octavos
		PartidoEuro2016.objects.create(usuario=instance, partido_id=37, local_id=1, visitante_id=5, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=38, local_id=2, visitante_id=6, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=39, local_id=9, visitante_id=13, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=40, local_id=10, visitante_id=14, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=41, local_id=17, visitante_id=21, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=42, local_id=18, visitante_id=22, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=43, local_id=25, visitante_id=29, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=44, local_id=26, visitante_id=30, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		#TODO: Hay que completar el resto de partidos: fase de cuartos, semis, ect...

		#Cuartos
		PartidoEuro2016.objects.create(usuario=instance, partido_id=45, local_id=1, visitante_id=2, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=46, local_id=9, visitante_id=10, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=47, local_id=17, visitante_id=18, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=48, local_id=25, visitante_id=26, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))

		#Semis
		PartidoEuro2016.objects.create(usuario=instance, partido_id=49, local_id=1, visitante_id=9, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))
		PartidoEuro2016.objects.create(usuario=instance, partido_id=50, local_id=17, visitante_id=25, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))		

		#Final
		PartidoEuro2016.objects.create(usuario=instance, partido_id=51, local_id=1, visitante_id=17, local=random.randrange(RESULTADO_DEFAULT), visitante=random.randrange(RESULTADO_DEFAULT))

        