from django.conf.urls import include, url

from django.contrib import admin

from home import views as home_views

urlpatterns = [
    
    url('^$', home_views.index, name='index'),    

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('home.urls')),
    url(r'^mundial2014/', include('mundial2014.urls')),
    url(r'^euro2016/', include('euro2016.urls')),
]
