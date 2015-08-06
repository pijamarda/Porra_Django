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

class PartidoEuro2016(models.Model):
	usuario = models.ForeignKey(User)
	partido_id = models.IntegerField()
	local_id = models.IntegerField()
	visitante_id = models.IntegerField()
	local = models.IntegerField()
	visitante = models.IntegerField()	
	
	def __str__(self):
		return str(self.partido_id)

class RankEuro2016(models.Model):
	usuario = models.ForeignKey(User, unique=True)
	puntos = models.IntegerField(default=0)
	a1 = models.IntegerField(default=0)
	a2 = models.IntegerField(default=0)
	b1 = models.IntegerField(default=0)
	b2 = models.IntegerField(default=0)
	c1 = models.IntegerField(default=0)
	c2 = models.IntegerField(default=0)
	d1 = models.IntegerField(default=0)
	d2 = models.IntegerField(default=0)
	e1 = models.IntegerField(default=0)
	e2 = models.IntegerField(default=0)
	f1 = models.IntegerField(default=0)
	f2 = models.IntegerField(default=0)

	def __str__(self):
		return str(self.usuario)
