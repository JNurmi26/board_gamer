"""Defines URL patterns for board_gamer."""

from django.urls import path
from . import views

app_name = 'board_gamer'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Games page
    path('games/', views.games, name='games'),
]