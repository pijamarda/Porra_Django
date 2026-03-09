from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from tournaments.models import Tournament


def index(request):
	tournaments = Tournament.objects.all().order_by('-year')
	return render(request, "home/index.html", {'tournaments': tournaments})

# Utilizado para el registro de nuevos usuarios
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/tournaments/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {'form': form })