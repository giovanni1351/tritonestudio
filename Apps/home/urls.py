from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index, name="index"),
    # path('teste',views.index2, name="index"),
    # path('DrunkWiz',views.drunkwiz, name="Drunk Wiz"),
    path('', views.home, name='home'),
    path('jogo/<slug:slug>/', views.game_detail, name='game_detail'),
    path('jogar/<int:id>/', views.jogar, name='Jogar'),
]