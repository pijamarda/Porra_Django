from operator import itemgetter, attrgetter

from .models import PartidoEuro2016, RankEuro2016
#BORRAR: he añadido los equipos y grupos del proyecto anterior para nos escribirlos a mano
# una vez tengamos los de verdad se agregaran en el panel admin
from mundial2014.models import Equipo, Grupo

'''
	Aunque podria utilizar un diccionario normal, esta clase me permite visualizar facilmente
	el modelo de datos de equipos que quiero mandar a las vistas
'''
class CEquipo:
	equipo_id = 0
	puntos = 0
	ganados = 0
	empatados = 0
	perdidos = 0
	favor = 0
	contra = 0
	diff = 0
	name = "Spain"
	flag = "es"


def actualizar_grupo(pk_grupo_id, usuario):
	
	
	grupo = Grupo.objects.get(grupo_id=pk_grupo_id)
	
	equipos_grupo = Equipo.objects.filter(grupo=grupo.id)
	partidos_fase_grupos = get_partidos_fase_grupos(grupo.grupo_id, usuario)
	
	#teams guarda los equipos del grupo que vamos a analizar
	# y guardamos varios datos del equipo para luego utilizarlos en la vista
	teams = []
	for e in equipos_grupo:
		team = CEquipo()
		team.equipo_id = e.equipo_id
		team.name = e.name
		team.flag = e.flag
		teams.append(team)		

	for partido in partidos_fase_grupos:		
		partido_temp = PartidoEuro2016.objects.get(pk=partido)
		local_goles = partido_temp.local
		visitante_goles = partido_temp.visitante
		if (local_goles > visitante_goles):
			for team in teams:
				if (team.equipo_id == partido_temp.local_id):
					team.puntos += 3
					team.ganados += 1
				elif (team.equipo_id == partido_temp.visitante_id):
					team.perdidos += 1
		elif (local_goles < visitante_goles):
			for team in teams:
				if (team.equipo_id == partido_temp.visitante_id):
					team.puntos += 3
					team.ganados += 1
				elif (team.equipo_id == partido_temp.local_id):
					team.perdidos += 1
		else:
			for team in teams:
				if (team.equipo_id == partido_temp.local_id):
					team.puntos += 1
					team.empatados += 1
				elif (team.equipo_id == partido_temp.visitante_id):
					team.puntos += 1
					team.empatados += 1
		#Ahora voy a actualizar los goles a favor y en contra de los equipos para mostrarlos
		# en la vista de la fase de grupos, y en caso de empate poder utilizar estos datos
		# como desempate
		for team in teams:
				if (team.equipo_id == partido_temp.local_id):
					team.favor += local_goles
					team.contra += visitante_goles
					team.diff = team.favor - team.contra
				elif (team.equipo_id == partido_temp.visitante_id):
					team.favor += visitante_goles
					team.contra += local_goles
					team.diff = team.favor - team.contra

	# Para saber quien va primero vamos a utilizar la funcion sorted de Python lo que nos permite
	# ordenar una lista por varios criterios de prioridad
	ordenados = sorted(teams, key=attrgetter('puntos', 'diff','favor'), reverse=True)
	
	primero = ordenados[0]
	segundo = ordenados[1]
	teams_pasan = []
	teams_pasan.append([primero.equipo_id,primero.name])
	teams_pasan.append([segundo.equipo_id,segundo.name])

	grupo_id = grupo.id	
	#Ahora recorro los grupos y segun el grupo marco los partidos como deben ser
	#jugados en la fase de octavos
	if (grupo_id == 1):				
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=49)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=50)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 2):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=50)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=49)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 3):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=51)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=52)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 4):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=52)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=51)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 5):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=53)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=54)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 6):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=54)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=53)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 7):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=55)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=56)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 8):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=56)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=55)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	
	#Ahora vamos a recorrer los octavos y actualizar los equipos que pasan a cuartos
	#lo que hago es comparar simplemente los resultados de la fase de cuartos

	partidos = PartidoEuro2016.objects.filter(usuario=usuario)
	for partido in partidos:
		if (partido.partido_id == 49):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=57)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		if (partido.partido_id == 50):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=57)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()

	datos = []
	datos.append(ordenados)
	datos.append(teams_pasan)

	return datos

'''
	Funcion auxiliar que te permite calcular el ID de los partidos segun el grupo
	devuelve un array con los ID de los partidos del grupo buscado asignado al usuario
'''
def get_partidos_fase_grupos(grupo_id,usuario):
	
	partidos = PartidoEuro2016.objects.filter(usuario = usuario).order_by("partido_id")
	partidos_grupo = []
	#Grupo A id=1
	if (grupo_id==1):
		for partido in partidos:
			if (partido.partido_id in [1,2,14,15,25,26]):
				partidos_grupo.append(partido.pk)
	#Grupo B id=2
	elif (grupo_id==2):
		for partido in partidos:
			if (partido.partido_id in [3,4,13,16,27,28]):
				partidos_grupo.append(partido.pk)
	#Grupo C id=3
	elif (grupo_id==3):
		for partido in partidos:
			if (partido.partido_id in [6,7,17,18,29,30]):
				partidos_grupo.append(partido.pk)
	#Grupo D id=4
	elif (grupo_id==4):
		for partido in partidos:
			if (partido.partido_id in [5,8,20,21,31,32]):
				partidos_grupo.append(partido.pk)
	#Grupo E id=5
	elif (grupo_id==5):
		for partido in partidos:
			if (partido.partido_id in [9,10,19,22,35,36]):
				partidos_grupo.append(partido.pk)
	#Grupo F id=6
	elif (grupo_id==6):
		for partido in partidos:
			if (partido.partido_id in [11,12,23,24,33,34]):
				partidos_grupo.append(partido.pk)

	return(partidos_grupo)