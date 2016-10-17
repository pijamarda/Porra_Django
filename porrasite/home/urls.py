from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views

from home import views as home_views

urlpatterns = [        
    url('^login/$', auth_views.login, name='login'),
    url('^logout/$', auth_views.logout, {'next_page': '/euro2016'}),
    url('^new/$', home_views.register, name='register'),
]