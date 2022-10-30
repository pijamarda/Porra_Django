from django.urls import include, path

from django.contrib import admin
from django.contrib.auth import views as auth_views

from home import views as home_views

urlpatterns = [        
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/euro2016'}, name='logout'),
    path('new/', home_views.register, name='register'),
]