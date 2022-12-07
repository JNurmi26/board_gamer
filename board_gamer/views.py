from django.shortcuts import render

from .models import Game

# Create your views here.
def index(request):
    """The home page for Board Gamer"""
    return render(request, 'board_gamer/index.html')

def games(request):
    """Show all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_gamer/games.html', context)