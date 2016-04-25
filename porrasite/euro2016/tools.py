from operator import itemgetter, attrgetter

from .models import PartidoEuro2016, RankEuro2016
#BORRAR: he añadido los equipos y grupos del proyecto anterior para nos escribirlos a mano
# una vez tengamos los de verdad se agregaran en el panel admin
from euro2016.models import Equipo, Grupo

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
	pasa = 0
	grupo = 0
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
		team.name = e.nombre
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

	grupo_id = pk_grupo_id	
	#Ahora recorro los grupos y segun el grupo marco los partidos como deben ser
	#jugados en la fase de octavos, ojo que no siempre hay que modificarlo ya que
	# tambien hay que tener en cuenta la fase de 3rd
	if (grupo_id == 1):				
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=37)
		partido_temp.local_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 2):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=44)
		partido_temp.local_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 3):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=37)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 4):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=43)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 5):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=43)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=42)
		partido_temp.visitante_id=segundo.equipo_id
		partido_temp.save()
	elif (grupo_id == 6):		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=42)
		partido_temp.local_id=primero.equipo_id
		partido_temp.save()		
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=44)
		partido_temp.visitante_id=segundo.equipo_id
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

'''
	Funcion auxiliar que nos permite calcular quienes de los terceros de grupo pasan a la siguiente ronda
'''

def actualizar_grupo_3rd(usuario):
		
	teams_3rd = []
	#Tengo que recorrer todos los grupos
	grupos = Grupo.objects.all()
	for grupo in grupos:
		#
		equipos_grupo = Equipo.objects.filter(grupo=grupo.id)
		partidos_fase_grupos = get_partidos_fase_grupos(grupo.grupo_id, usuario)
		
		#teams guarda los equipos del grupo que vamos a analizar
		# y guardamos varios datos del equipo para luego utilizarlos en la vista
		teams = []
		for e in equipos_grupo:
			team = CEquipo()
			team.equipo_id = e.equipo_id
			team.name = e.nombre
			team.flag = e.flag
			team.grupo = grupo.grupo_id
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
		
		tercero = ordenados[2]		
		teams_3rd.append(tercero)	

	# Ordeno la tabla de equipos segun los criterios Uefa
	teams_3rd_ordenados = sorted(teams_3rd, key=attrgetter('puntos', 'diff','favor'), reverse=True)
	# A los equpos que pasan les pongo una marca para que se vea claro en la vista cuales son
	teams_3rd_ordenados[0].pasa = 1
	teams_3rd_ordenados[1].pasa = 1
	teams_3rd_ordenados[2].pasa = 1
	teams_3rd_ordenados[3].pasa = 1

	#Creo una nueva lista con solo los 4 equipos que pasan
	teams_3rd_grupos = []
	teams_3rd_grupos.append(teams_3rd_ordenados[0])
	teams_3rd_grupos.append(teams_3rd_ordenados[1])
	teams_3rd_grupos.append(teams_3rd_ordenados[2])
	teams_3rd_grupos.append(teams_3rd_ordenados[3])
	#Ahora voy a ordenar los equipos segun su grupo_id
	teams_3rd_grupos = sorted(teams_3rd_grupos, key=attrgetter('grupo'))
	for t in teams_3rd_grupos:
		print(t.grupo)
	# Ahora utilizando la guia de la Wikipedia puedo realizar los emparejamientos correctamente
	# Utilizo un nombre de variable muy pequeño para que no ocupe tanto
	t3g = teams_3rd_grupos
	# Si pasan los equipos de los grupos ABCD
	if (t3g[0].grupo == 1 and t3g[1].grupo == 2 and t3g[2].grupo == 3 and t3g[3].grupo == 4):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		print("pasan: ABCD")
	# Si pasan los equipos de los grupos ABCE
	if (t3g[0].grupo == 1 and t3g[1].grupo == 2 and t3g[2].grupo == 3 and t3g[3].grupo == 5):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ABCE")
	# Si pasan los equipos de los grupos ABCF
	if (t3g[0].grupo == 1 and t3g[1].grupo == 2 and t3g[2].grupo == 3 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ABCF")
	# Si pasan los equipos de los grupos ABDE
	if (t3g[0].grupo == 1 and t3g[1].grupo == 2 and t3g[2].grupo == 4 and t3g[3].grupo == 5):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ABDE")
	# Si pasan los equipos de los grupos ABDF
	if (t3g[0].grupo == 1 and t3g[1].grupo == 2 and t3g[2].grupo == 4 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ABDF")
	# Si pasan los equipos de los grupos ABEF
	if (t3g[0].grupo == 1 and t3g[1].grupo == 2 and t3g[2].grupo == 5 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ABEF")
	# Si pasan los equipos de los grupos ACDE
	if (t3g[0].grupo == 1 and t3g[1].grupo == 3 and t3g[2].grupo == 4 and t3g[3].grupo == 5):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ACDE")
	# Si pasan los equipos de los grupos ACDF
	if (t3g[0].grupo == 1 and t3g[1].grupo == 3 and t3g[2].grupo == 4 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: ACDF")
	# Si pasan los equipos de los grupos ACEF
	if (t3g[0].grupo == 1 and t3g[1].grupo == 3 and t3g[2].grupo == 5 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		print("pasan: ACEF")
	# Si pasan los equipos de los grupos ADEF
	if (t3g[0].grupo == 1 and t3g[1].grupo == 4 and t3g[2].grupo == 5 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		print("pasan: ADEF")
	# Si pasan los equipos de los grupos BCDE
	if (t3g[0].grupo == 2 and t3g[1].grupo == 3 and t3g[2].grupo == 4 and t3g[3].grupo == 5):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: BCDE")
	# Si pasan los equipos de los grupos BCDF
	if (t3g[0].grupo == 2 and t3g[1].grupo == 3 and t3g[2].grupo == 4 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: BCDF")
	# Si pasan los equipos de los grupos BCEF
	if (t3g[0].grupo == 2 and t3g[1].grupo == 3 and t3g[2].grupo == 5 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: BCEF")
	# Si pasan los equipos de los grupos BDEF
	if (t3g[0].grupo == 2 and t3g[1].grupo == 4 and t3g[2].grupo == 5 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		print("pasan: BDEF")
	# Si pasan los equipos de los grupos CDEF
	if (t3g[0].grupo == 3 and t3g[1].grupo == 4 and t3g[2].grupo == 5 and t3g[3].grupo == 6):
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=40)		
		partido_temp.visitante_id=t3g[0].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=38)		
		partido_temp.visitante_id=t3g[1].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=41)		
		partido_temp.visitante_id=t3g[3].equipo_id
		partido_temp.save()
		partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=39)		
		partido_temp.visitante_id=t3g[2].equipo_id
		partido_temp.save()
		print("pasan: CDEF")
	return teams_3rd_ordenados

# Funcion que actualiza todos los partidos de las elminatorias
def actualizar_eliminatorias(usuario):

	#Primero recorro la fase de octavos para ver quienes pasan a cuartos
	partidos = PartidoEuro2016.objects.filter(usuario=usuario)
	for partido in partidos:
		if (partido.partido_id == 37):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=45)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 38):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=46)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 39):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=45)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 40):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=48)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 41):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=47)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 42):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=46)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 43):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=47)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 44):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=48)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()
	for partido in partidos:
		#Recorro la fase de cuartos para ver quienes pasan a semis
		if (partido.partido_id == 45):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=49)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id				
			partido_temp.save()
		elif (partido.partido_id == 46):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=49)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id				
			partido_temp.save()
		elif (partido.partido_id == 47):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=50)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 48):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=50)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()
	for partido in partidos:
		#Recorro la fase de semis para ver quienes pasan a la final
		if (partido.partido_id == 49):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=51)
			if (partido.local > partido.visitante):				
				partido_temp.local_id = partido.local_id				
			else:
				partido_temp.local_id = partido.visitante_id
			partido_temp.save()
		elif (partido.partido_id == 50):
			partido_temp = PartidoEuro2016.objects.get(usuario=usuario, partido_id=51)
			if (partido.local > partido.visitante):				
				partido_temp.visitante_id = partido.local_id				
			else:
				partido_temp.visitante_id = partido.visitante_id
			partido_temp.save()
		#FINAL!