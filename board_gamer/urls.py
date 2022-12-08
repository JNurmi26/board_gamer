"""Defines URL patterns for board_gamer."""

from django.urls import path
from . import views

app_name = 'board_gamer'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Games page
    path('games/', views.games, name='games'),

    # Detail page for a single game
    path('games/<int:game_id>/', views.game, name='game'),

    # Page for adding a new board game
    path('new_game/', views.new_game, name='new_game'),
]