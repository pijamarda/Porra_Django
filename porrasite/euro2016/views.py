from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


from .models import PartidoEuro2016, RankEuro2016
#BORRAR: he añadido los equipos y grupos del proyetcto anterios para nos escribirlos a mano
# una vez tengamos los de verdad se agregaran en el panel admin
from mundial2014.models import Equipo, Grupo

#
from .tools import *

# Debug marca en principio:
#	- En los templates si queremos mostrar las columnas con los ID de la mayoria de los elementos
DEBUG = True

# Por ahora es nuestra pagina de inicio y muestra a todos los usuarios y sus puntos
def rank_list(request):
	ranking = RankEuro2016.objects.all().order_by('puntos').reverse()
	return render(request, 'euro2016/rank_list.html', {'ranking': ranking})

# Esta vista muestra todos los partidos de un usuario a traves de su 'pk'
def partido_list(request, pk):	
	usuario = User.objects.get(pk=pk)
	partidos = PartidoEuro2016.objects.filter(usuario = usuario).order_by('partido_id')
	equipos = Equipo.objects.all()
	grupos_todos = Grupo.objects.all().order_by('grupo_id')

	

	return render(request, 'euro2016/partido_list.html', {'partidos': partidos, 
															 'usuario': usuario, 
															 'equipos': equipos, 
															 'grupos_todos':grupos_todos, 
															 'debug': DEBUG})

# Muestra el detalle de un partido en concreto
def partido_detalle(request, pk, pk_user):
	partido = get_object_or_404(PartidoEuro2016, pk=pk)
	return render(request, 'euro2016/partido_detalle.html', {'partido': partido})

# Listado de todos los equipos
def equipo_list(request):	
	equipos = Equipo.objects.all()
	return render(request, 'euro2016/equipo_list.html', {'equipos': equipos})

# Listado de todos los grupos
def grupo_list(request):		
	grupos = Grupo.objects.all().order_by('grupo_id')
	equipos = Equipo.objects.all()
	return render(request, 'euro2016/grupo_list.html', {'grupos': grupos, 
														   'equipos': equipos})

# Esta vista muestra todos los partidos del usuario, ademas de la posibilidad de navegar
# por los grupos
def grupo_equipos(request, pk_grupo_id, pk_user):
	
	grupos = Grupo.objects.filter(grupo_id=pk_grupo_id)	
	equipos = Equipo.objects.all()
	equipos_grupo = Equipo.objects.filter(grupo=pk_grupo_id)
	partidos = PartidoEuro2016.objects.all().order_by('partido_id')
	usuario = User.objects.get(pk=pk_user)
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	partidos_fase_grupos = get_partidos_fase_grupos(grupos[0].grupo_id, usuario)	

	datos = []
	
	datos = actualizar_grupo(pk_grupo_id, usuario)

	teams = datos[0]
	teams_pasan = datos[1]	

	vengo_desde = 'grupos'

	return render(request, 'euro2016/grupo_equipos.html', {'grupos': grupos, 
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

# Esta vista es la de los terceros de grupo para ir probando
def grupo_3rd(request, pk_user):			
	
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	usuario = User.objects.get(pk=pk_user)
	datos = actualizar_grupo_3rd(pk_user)	

	return render(request, 'euro2016/grupo_3rd.html', {'teams': datos,
														'usuario':usuario,
														'grupos_todos':grupos_todos,
														'debug':DEBUG,
														})


def partido_edit(request, pk, pk_user, desde):

	usuario = User.objects.get(pk=pk_user)
	partido = get_object_or_404(PartidoEuro2016, pk=pk)
	equipo = Equipo.objects.filter(equipo_id=partido.local_id)
	grupo_pk = 1
	for e in equipo:
		grupo_pk = e.grupo.pk
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	if request.method == "POST":
		form = PartidoEuro2016Form(request.POST, instance=partido)
		if form.is_valid():
			partido = form.save(commit=False)            
			partido.save()
			print (desde)
			if (desde == 'grupos'):
				return redirect('euro2016.views.grupo_equipos', pk=grupo_pk, pk_user=pk_user)
			elif (desde == 'eliminatorias'):
				return redirect('euro2016.views.eliminatorias', pk_user=pk_user)
	else:
		form = PartidoEuro2016Form(instance=partido)

	return render(request, 'euro2016/partido_edit.html', {'form': form,
															 'usuario':usuario,
															 'grupos_todos':grupos_todos})

def suma_puntos(request):
	
	cat_id = None
	if request.method == 'GET':		
		cat_id = request.GET['category_id']		

	likes = 0
	if cat_id:
		usuario = RankEuro2016.objects.get(id=int(cat_id))
		print(usuario)
		if usuario:
			likes = usuario.puntos + 1
			usuario.puntos =  likes
			usuario.save()

	return HttpResponse(likes)


'''
	Esta funcion sirve para modificar los partidos en modo AJAX, es decir sin tener que utilizar
	un formulario estandar, ni tener que abrir nueva ventana
	Funcionamiento:
'''
def edita_partido_ajax(request):
	
	partido_id = None
	local = 0
	visitante = 0
	# Primero nos traemos desde el GET las nuevas variables a modificar
	if request.method == 'GET':		
		partido_id = request.GET['partido_id']
		local = request.GET['local']
		visitante = request.GET['visitante']
	
	if partido_id:
		# Si existe el partido entonces buscamos el partido en la base de datos de partidos
		# este sera unico para el usuario
		partido = PartidoEuro2016.objects.get(id=int(partido_id))
		
		if partido:
			# Si ha encontrado el partido entonces modificamos con los nuevos valores de 
			# goles del local y del visitante
			partido.local = local
			partido.visitante = visitante
			partido.save()
			response = 'ok'			

	return HttpResponse(response)

def eliminatorias(request, pk_user, formato):	
	
	usuario = User.objects.get(pk=pk_user)
	rank = RankEuro2016.objects.get(usuario=pk_user)
	partidos = PartidoEuro2016.objects.filter(usuario=pk_user).order_by('partido_id')
	equipos = Equipo.objects.all()	
	vengo_desde = 'eliminatorias'
	#print(equipos_grupo)
	grupos_todos = Grupo.objects.all().order_by('grupo_id')
	for gr in grupos_todos:
		actualizar_grupo(gr.grupo_id, usuario)

	template_to_render = 'euro2016/eliminatorias_lista.html'
	if (formato == 'tabla'):
		template_to_render = 'euro2016/eliminatorias_tabla.html'

	return render(request, template_to_render, {'usuario': usuario,
														'rank': rank,
														'partidos': partidos,
														'equipos': equipos
														})