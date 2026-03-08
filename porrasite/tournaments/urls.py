from django.urls import path
from . import views

app_name = 'tournaments'

urlpatterns = [
    path('', views.tournament_list, name='list'),
    path('<slug:slug>/', views.tournament_index, name='index'),
    path('<slug:slug>/knockout/', views.knockout, name='knockout'),
    path('<slug:slug>/ranking/', views.ranking, name='ranking'),
    path('<slug:slug>/groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('<slug:slug>/predictions/<int:match_id>/save/', views.prediction_save, name='prediction_save'),
    path('<slug:slug>/knockout/<int:match_id>/save/', views.knockout_prediction_save, name='knockout_prediction_save'),
]
