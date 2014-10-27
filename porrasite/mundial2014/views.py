from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .forms import PartidoForm

from .models import Partido, Rank, Equipo, Grupo

# Create your views here.

#Aqui asociamos a cada grupo el partido_id de la lista de partidos
#con lo que

DEBUG = False

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
	#marcamos quienes pasan de fase en el Grupo A
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


def partido_list(request, pk):
	
	usuario = User.objects.get(pk=pk)
	partidos = Partido.objects.filter(usuario = usuario).order_by('partido_id')
	equipos = Equipo.objects.all()
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	return render(request, 'mundial2014/partido_list.html', {'partidos': partidos, 'usuario': usuario, 'equipos': equipos, 'grupos_todos':grupos_todos, 'debug': DEBUG})

def partido_detalle(request, pk, pk_user):

	partido = get_object_or_404(Partido, pk=pk)
	return render(request, 'mundial2014/partido_detalle.html', {'partido': partido})

def rank_list(request):

	ranking = Rank.objects.all().order_by('puntos').reverse()
	return render(request, 'mundial2014/rank_list.html', {'ranking': ranking})

def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/mundial/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {'form': form })

def equipo_list(request):	
	
	equipos = Equipo.objects.all()
	return render(request, 'mundial2014/equipo_list.html', {'equipos': equipos})

def grupo_list(request):	
	
	grupos = Grupo.objects.all().order_by('grupo_id')
	equipos = Equipo.objects.all()
	return render(request, 'mundial2014/grupo_list.html', {'grupos': grupos, 'equipos': equipos})

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
	actualizar_grupo(grupo_id, usuario, teams)

	return render(request, 'mundial2014/grupo_equipos.html', {'grupos': grupos, 'equipos': equipos, 'usuario':usuario, 'grupos_todos':grupos_todos, 'partidos': partidos, 'partidos_fase_grupos':partidos_fase_grupos, 'teams': teams, 'debug':DEBUG})


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

	return render(request, 'mundial2014/partido_edit.html', {'form': form, 'usuario':usuario, 'grupos_todos':grupos_todos})

