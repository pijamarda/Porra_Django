from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.rank_list),
	
    #url(r'^partido/', views.partido_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.partido_list),
    #url(r'^user/(?P<pk>[0-9]+)/edit/$', views.partido_edit),
    url(r'^user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/$', views.partido_detalle),
    url(r'^user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_grupos$', views.partido_edit, {'desde': 'grupos'}, name='partido_edit_group'),
    url(r'^user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_octavos$', views.partido_edit, {'desde': 'octavos'}, name='partido_edit_octavos'),
    url(r'^user/(?P<pk_user>[0-9]+)/grupo/(?P<pk>[0-9]+)/$', views.grupo_equipos),
    url(r'^user/(?P<pk_user>[0-9]+)/octavos/$', views.octavos, {'formato': 'normal'}, name='eliminatorias_lista'),
    url(r'^user/(?P<pk_user>[0-9]+)/octavos/tabla$', views.octavos, {'formato': 'tabla'}, name='eliminatorias_tabla'),
    url(r'^equipos/$', views.equipo_list),
    url(r'^grupos/$', views.grupo_list),
    url(r'^suma_puntos/$', views.suma_puntos, name='suma_puntos'),
    url(r'^edita_partido_ajax/$', views.edita_partido_ajax, name='edita_partido_ajax'),
]