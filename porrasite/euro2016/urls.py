from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
	url(r'^$', views.rank_list),
	
    #url(r'^partido/', views.partido_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.partido_list),
    #url(r'^user/(?P<pk>[0-9]+)/edit/$', views.partido_edit),
    url(r'^user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/$', views.partido_detalle),
    url(r'^user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_grupos$', views.partido_edit, {'desde': 'grupos'}, name='partido_edit_group'),
    url(r'^user/(?P<pk_user>[0-9]+)/partido/(?P<pk>[0-9]+)/edit_eliminatorias$', views.partido_edit, {'desde': 'eliminatorias'}, name='partido_edit_eliminatorias'),
    url(r'^user/(?P<pk_user>[0-9]+)/grupo/(?P<pk_grupo_id>[0-9]+)/$', views.grupo_equipos),  
    url(r'^user/(?P<pk_user>[0-9]+)/grupo/3rd/$', views.grupo_3rd),  
    url(r'^user/(?P<pk_user>[0-9]+)/eliminatorias/$', views.eliminatorias, {'formato': 'normal'}, name='eliminatorias_lista'),
    url(r'^user/(?P<pk_user>[0-9]+)/eliminatorias/tabla$', views.eliminatorias, {'formato': 'tabla'}, name='eliminatorias_tabla'),
    url(r'^equipos/$', views.equipo_list),
    url(r'^grupos/$', views.grupo_list),
    url(r'^suma_puntos/$', views.suma_puntos, name='suma_puntos'),
    url(r'^edita_partido_ajax/$', views.edita_partido_ajax, name='edita_partido_ajax'),
    url(r'^list_partido_ajax/$', views.list_partido_ajax, name='list_partido_ajax'),
)