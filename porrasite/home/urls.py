from django.conf.urls import patterns, include, url

from django.contrib import admin

from home import views


urlpatterns = patterns('',    
    
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/euro2016'}),
    url(r'^new/$', 'home.views.register'),
)