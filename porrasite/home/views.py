from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
	
	return render(request, "home/index.html", {})

# Utilizado para el registro de nuevos usuarios
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {'form': form })