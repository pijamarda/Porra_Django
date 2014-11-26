from .models import Partido, Rank, Equipo, Grupo

class CEquipo:
	equipo_id = 0
	puntos = 0
	ganados = 0
	empatados = 0
	perdidos = 0
	name = "Spain"
	flag = "es"

def actualizar_grupo(grupo_id, usuario, teams):
	rank = Rank.objects.get(usuario=usuario)

	primero = teams[0]
	segundo = teams[1]
	temporal = teams[2]
	for team in teams:
		if (team.puntos > primero.puntos):
			temporal = primero
			primero = team
			segundo = temporal
		elif (team.puntos > segundo.puntos and team.equipo_id != primero.equipo_id):
			segundo = team
	print("Primero " + primero.name)
	print("Segundo " + segundo.name)
	teams_passan = []
	teams_passan.append([primero.equipo_id,primero.name])
	teams_passan.append([segundo.equipo_id,segundo.name])
	#marcamos quienes pasan de fase segun su grupo
	if (grupo_id == 1):		
		rank.a1=primero.equipo_id
		rank.a2=segundo.equipo_id		
	elif (grupo_id == 2):		
		rank.b1=primero.equipo_id
		rank.b2=segundo.equipo_id
	elif (grupo_id == 3):		
		rank.c1=primero.equipo_id
		rank.c2=segundo.equipo_id
	elif (grupo_id == 4):		
		rank.d1=primero.equipo_id
		rank.d2=segundo.equipo_id
	elif (grupo_id == 5):		
		rank.e1=primero.equipo_id
		rank.e2=segundo.equipo_id
	elif (grupo_id == 6):		
		rank.f1=primero.equipo_id
		rank.f2=segundo.equipo_id
	elif (grupo_id == 7):		
		rank.g1=primero.equipo_id
		rank.g2=segundo.equipo_id	
	elif (grupo_id == 8):		
		rank.h1=primero.equipo_id
		rank.h2=segundo.equipo_id	
	rank.save()
	return teams_passan

def get_partidos_fase_grupos(grupo_id,usuario):
	
	partidos = Partido.objects.filter(usuario = usuario).order_by("partido_id")
	partidos_grupo = []
	#Grupo A id=1
	if (grupo_id==1):
		for partido in partidos:
			if (partido.partido_id in [1,2,17,18,33,34]):
				partidos_grupo.append(partido.pk)
	#Grupo B id=2
	elif (grupo_id==2):
		for partido in partidos:
			if (partido.partido_id in [3,4,20,19,35,36]):
				partidos_grupo.append(partido.pk)
	#Grupo C id=3
	elif (grupo_id==3):
		for partido in partidos:
			if (partido.partido_id in [5,6,21,22,37,38]):
				partidos_grupo.append(partido.pk)
	#Grupo D id=4
	elif (grupo_id==4):
		for partido in partidos:
			if (partido.partido_id in [7,8,23,24,39,40]):
				partidos_grupo.append(partido.pk)
	#Grupo E id=5
	elif (grupo_id==5):
		for partido in partidos:
			if (partido.partido_id in [9,10,25,26,41,42]):
				partidos_grupo.append(partido.pk)
	#Grupo F id=6
	elif (grupo_id==6):
		for partido in partidos:
			if (partido.partido_id in [11,12,27,28,43,44]):
				partidos_grupo.append(partido.pk)
	#Grupo G id=7
	elif (grupo_id==7):
		for partido in partidos:
			if (partido.partido_id in [13,14,29,30,45,46]):
				partidos_grupo.append(partido.pk)
	#Grupo H id=8
	elif (grupo_id==8):
		for partido in partidos:
			if (partido.partido_id in [15,16,31,32,47,48]):
				partidos_grupo.append(partido.pk)
	return(partidos_grupo)