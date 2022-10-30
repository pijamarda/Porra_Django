from django.urls import include, path, re_path
from django.contrib import admin

from . import views

urlpatterns = [
	path('', views.index),
	
    path('rank/', views.rank_list),
    re_path('user/(?P<pk>[0-9]+)/$', views.partido_list, name='partido_list'),
    #url(r'^user/(?P<pk>[0-9]+)/edit/$', views.partido_edit),
    re_path('user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/$', views.partido_detalle, name='partido_detalle'),
    re_path('user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_grupos', views.partido_edit, {'desde': 'grupos'}, name='partido_edit_group'),
    re_path('user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_eliminatorias', views.partido_edit, {'desde': 'eliminatorias'}, name='partido_edit_eliminatorias'),
    re_path('user/(?P<pk_user>[0-9]+)/grupo/(?P<pk_grupo_id>[0-9]+)/$', views.grupo_equipos, name='grupo_equipos'),  
    re_path('user/(?P<pk_user>[0-9]+)/grupo/3rd/$', views.grupo_3rd, name='grupo_3rd'),  
    re_path('user/(?P<pk_user>[0-9]+)/eliminatorias/$', views.eliminatorias, {'formato': 'normal'}, name='eliminatorias_lista'),
    re_path('user/(?P<pk_user>[0-9]+)/eliminatorias/tabla', views.eliminatorias, {'formato': 'tabla'}, name='eliminatorias_tabla'),
    path('equipos/', views.equipo_list),
    path('grupos/', views.grupo_list),
    path('suma_puntos/', views.suma_puntos, name='suma_puntos'),
    path('edita_partido_ajax/', views.edita_partido_ajax, name='edita_partido_ajax'),
    path('list_partido_ajax/', views.list_partido_ajax, name='list_partido_ajax'),
]