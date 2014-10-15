from django.contrib import admin

from .models import Partido, Equipo, Rank, Grupo

# Register your models here.

admin.site.register(Partido)
admin.site.register(Equipo)
admin.site.register(Rank)
admin.site.register(Grupo)
