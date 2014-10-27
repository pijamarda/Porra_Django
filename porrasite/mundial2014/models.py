from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grupo(models.Model):
	grupo_id = models.IntegerField()
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	grupo = models.ForeignKey(Grupo)
	equipo_id = models.IntegerField()	
	nombre = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	flag = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Partido(models.Model):
	usuario = models.ForeignKey(User)
	partido_id = models.IntegerField()
	local_id = models.IntegerField()
	visitante_id = models.IntegerField()
	local = models.IntegerField()
	visitante = models.IntegerField()	
	
	def __str__(self):
		return str(self.partido_id)

class Rank(models.Model):
	usuario = models.ForeignKey(User, unique=True)
	puntos = models.IntegerField()
	a1 = models.IntegerField()
	a2 = models.IntegerField()
	b1 = models.IntegerField()
	b2 = models.IntegerField()

	def __str__(self):
		return str(self.usuario)