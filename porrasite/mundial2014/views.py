from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


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

	datos = []
	
	datos = actualizar_grupo(pk, usuario)

	teams = datos[0]
	teams_pasan = datos[1]	

	vengo_desde = 'grupos'

	return render(request, 'mundial2014/grupo_equipos.html', {'grupos': grupos, 
															  'equipos': equipos, 
															  'usuario':usuario, 
															  'grupos_todos':grupos_todos, 
															  'partidos': partidos, 
															  'partidos_fase_grupos':partidos_fase_grupos, 
															  'teams': teams,
															  'debug':DEBUG,
															  'teams_pasan': teams_pasan,
															  'vengo_desde': vengo_desde,
															  })

def partido_edit(request, pk, pk_user, desde):

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
			print (desde)
			if (desde == 'grupos'):
				return redirect('mundial2014.views.grupo_equipos', pk=grupo_pk, pk_user=pk_user)
			elif (desde == 'octavos'):
				return redirect('mundial2014.views.octavos', pk_user=pk_user)
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

def edita_partido_ajax(request):
	
	partido_id = None
	local = 0
	visitante = 0
	if request.method == 'GET':		
		partido_id = request.GET['partido_id']
		local = request.GET['local']
		visitante = request.GET['visitante']
	
	if partido_id:
		partido = Partido.objects.get(id=int(partido_id))
		print(partido)
		if partido:
			#likes = usuario.puntos + 1
			#usuario.puntos =  likes
			#usuario.save()
			#likes = partido.id

			partido.local = local
			partido.visitante = visitante
			partido.save()
			response = 'ok'
			#response['ida'] = response.write('33')
			#response['vuelta'] = response.write('77')
			#data = {'33','77'};

	return HttpResponse(response)

def octavos(request, pk_user, formato):
	
	
	usuario = User.objects.get(pk=pk_user)
	rank = Rank.objects.get(usuario=pk_user)
	partidos = Partido.objects.filter(usuario=pk_user).order_by('partido_id')
	equipos = Equipo.objects.all()	
	vengo_desde = 'octavos'
	#print(equipos_grupo)
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	for gr in grupos_todos:
		actualizar_grupo(gr.pk, usuario)

	template_to_render = 'mundial2014/octavos.html'
	if (formato == 'tabla'):
		template_to_render = 'mundial2014/eliminatorias.html'

	return render(request, template_to_render, {'usuario': usuario,
														'rank': rank,
														'partidos': partidos,
														'equipos': equipos
														})