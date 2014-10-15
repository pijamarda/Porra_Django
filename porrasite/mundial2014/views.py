from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .forms import PartidoForm

from .models import Partido, Rank, Equipo, Grupo

# Create your views here.

def partido_list(request, pk):
	
	usuario = User.objects.get(pk=pk)
	partidos = Partido.objects.filter(usuario = usuario).order_by('partido_id')
	equipos = Equipo.objects.all()
	return render(request, 'mundial2014/partido_list.html', {'partidos': partidos, 'usuario': usuario, 'equipos': equipos})

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
	
	grupos = Grupo.objects.all()
	equipos = Equipo.objects.all()
	return render(request, 'mundial2014/grupo_list.html', {'grupos': grupos, 'equipos': equipos})

def partido_edit(request, pk, pk_user):

	partido = get_object_or_404(Partido, pk=pk)
	if request.method == "POST":
		form = PartidoForm(request.POST, instance=partido)
		if form.is_valid():
			partido = form.save(commit=False)            
			partido.save()
			return redirect('mundial2014.views.partido_detalle', pk=pk, pk_user=pk_user)
	else:
		form = PartidoForm(instance=partido)

	return render(request, 'mundial2014/partido_edit.html', {'form': form})