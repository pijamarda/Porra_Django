from django.urls import include, path, re_path
from django.contrib import admin

from . import views

urlpatterns = [
	path('', views.rank_list),
	
    #url(r'^partido/', views.partido_list),
    re_path('user/(?P<pk>[0-9]+)/', views.partido_list),
    #url(r'^user/(?P<pk>[0-9]+)/edit/$', views.partido_edit),
    re_path('user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/', views.partido_detalle),
    re_path('user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_grupos', views.partido_edit, {'desde': 'grupos'}, name='partido_edit_group'),
    re_path('user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_octavos', views.partido_edit, {'desde': 'octavos'}, name='partido_edit_octavos'),
    re_path('user/(?P<pk_user>[0-9]+)/grupo/(?P<pk>[0-9]+)/', views.grupo_equipos),
    re_path('user/(?P<pk_user>[0-9]+)/octavos/', views.octavos, {'formato': 'normal'}, name='eliminatorias_lista'),
    re_path('user/(?P<pk_user>[0-9]+)/octavos/tabla', views.octavos, {'formato': 'tabla'}, name='eliminatorias_tabla'),
    path('equipos/', views.equipo_list),
    path('grupos/', views.grupo_list),
    path('suma_puntos/', views.suma_puntos, name='suma_puntos'),
    path('edita_partido_ajax/', views.edita_partido_ajax, name='edita_partido_ajax'),
]