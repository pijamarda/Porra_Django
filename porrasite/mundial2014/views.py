from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


from .forms import PartidoForm

from .models import Partido, Rank, Equipo, Grupo

#
from .tools import *

# Create your views here.

# Debug marca en principio:
#	- En los templates si queremos mostrar las columnas con los ID de la mayoria de los elementos
DEBUG = True

# Por ahora es nuestra pagina de inicio y muestra a todos los usuarios y sus puntos
def rank_list(request):
	ranking = Rank.objects.all().order_by('puntos').reverse()
	return render(request, 'mundial2014/rank_list.html', {'ranking': ranking})

# Esta vista muestra todos los partidos de un usuario a traves de su 'pk'
def partido_list(request, pk):	
	usuario = User.objects.get(pk=pk)
	partidos = Partido.objects.filter(usuario = usuario).order_by('partido_id')
	equipos = Equipo.objects.all()
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	return render(request, 'mundial2014/partido_list.html', {'partidos': partidos, 
															 'usuario': usuario, 
															 'equipos': equipos, 
															 'grupos_todos':grupos_todos, 
															 'debug': DEBUG})

# Muestra el detalle de un partido en concreto
def partido_detalle(request, pk, pk_user):
	partido = get_object_or_404(Partido, pk=pk)
	return render(request, 'mundial2014/partido_detalle.html', {'partido': partido})

# Utilizado para el registro de nuevos usuarios
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/mundial/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {'form': form })

# Listado de todos los equipos
def equipo_list(request):	
	equipos = Equipo.objects.all()
	return render(request, 'mundial2014/equipo_list.html', {'equipos': equipos})

# Listado de todos los grupos
def grupo_list(request):		
	grupos = Grupo.objects.all().order_by('grupo_id')
	equipos = Equipo.objects.all()
	return render(request, 'mundial2014/grupo_list.html', {'grupos': grupos, 
														   'equipos': equipos})

# Esta vista muestra todos los partidos del usuario, ademas de la posibilidad de navegar
# por los grupos
def grupo_equipos(request, pk, pk_user):
	
	grupos = Grupo.objects.filter(pk=pk)	
	equipos = Equipo.objects.all()
	equipos_grupo = Equipo.objects.filter(grupo=pk)
	partidos = Partido.objects.all().order_by('partido_id')
	usuario = User.objects.get(pk=pk_user)
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	partidos_fase_grupos = get_partidos_fase_grupos(grupos[0].grupo_id, usuario)
	
	#print(equipos_grupo)

	teams = []
	for e in equipos_grupo:
		team = CEquipo()
		team.equipo_id = e.equipo_id
		team.name = e.name
		team.flag = e.flag
		teams.append(team)		

	for partido in partidos_fase_grupos:		
		partido_temp = Partido.objects.get(pk=partido)
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
	
	grupo_id = grupos[0].id
	teams_pasan = []
	teams_pasan = actualizar_grupo(grupo_id, usuario, teams)
	print(teams_pasan)

	return render(request, 'mundial2014/grupo_equipos.html', {'grupos': grupos, 
															  'equipos': equipos, 
															  'usuario':usuario, 
															  'grupos_todos':grupos_todos, 
															  'partidos': partidos, 
															  'partidos_fase_grupos':partidos_fase_grupos, 
															  'teams': teams, 'debug':DEBUG,
															  'teams_pasan': teams_pasan,
															  })

def partido_edit(request, pk, pk_user):

	usuario = User.objects.get(pk=pk_user)
	partido = get_object_or_404(Partido, pk=pk)
	equipo = Equipo.objects.filter(equipo_id=partido.local_id)
	grupo_pk = 1
	for e in equipo:
		grupo_pk = e.grupo.pk
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	if request.method == "POST":
		form = PartidoForm(request.POST, instance=partido)
		if form.is_valid():
			partido = form.save(commit=False)            
			partido.save()
			return redirect('mundial2014.views.grupo_equipos', pk=grupo_pk, pk_user=pk_user)
	else:
		form = PartidoForm(instance=partido)

	return render(request, 'mundial2014/partido_edit.html', {'form': form,
															 'usuario':usuario,
															 'grupos_todos':grupos_todos})

def suma_puntos(request):
	
	cat_id = None
	if request.method == 'GET':		
		cat_id = request.GET['category_id']		

	likes = 0
	if cat_id:
		usuario = Rank.objects.get(id=int(cat_id))
		print(usuario)
		if usuario:
			likes = usuario.puntos + 1
			usuario.puntos =  likes
			usuario.save()

	return HttpResponse(likes)

def octavos(request, pk_user):
	
	
	usuario = User.objects.get(pk=pk_user)
	rank = Rank.objects.get(usuario=pk_user)
	partidos = Partido.objects.filter(usuario=pk_user)
	equipos = Equipo.objects.all()
	#print(equipos_grupo)

	

	return render(request, 'mundial2014/octavos.html', {'usuario': usuario,
														'rank': rank,
														'partidos': partidos,
														'equipos': equipos
														})