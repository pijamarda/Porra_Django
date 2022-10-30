from django.contrib import admin
from django.urls import path

from django.urls import include

from home import views as home_views

urlpatterns = [
    
    path('', home_views.index, name='index'),    

    path('admin/', admin.site.urls),

    path('accounts/', include('home.urls')),
    path('mundial2014/', include('mundial2014.urls')),
    path('euro2016/', include('euro2016.urls')),
]
