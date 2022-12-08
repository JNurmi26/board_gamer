from django.shortcuts import render, redirect

from .models import Game
from .forms import GameForm

# Create your views here.
def index(request):
    """The home page for Board Gamer"""
    return render(request, 'board_gamer/index.html')

def games(request):
    """Show all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_gamer/games.html', context)

def game(request, game_id):
    """Show a single game"""
    print(game_id)
    game = Game.objects.get(id=game_id)
    context = {'game':game}
    return render(request, 'board_gamer/game.html', context)

def new_game(request):
    """Add a new game"""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = GameForm()
    else:
        # POST data submitted, process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_gamer:games')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_gamer/new_game.html', context)

def edit_game(request, game_id):
    """Edit an existing game."""
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        # Initial request, pre-fill form with current game info.
        form = GameForm(instance=game)
    else:
        # POST data submitted, process data.
        if form.is_valid():
            form.save
            return redirect('board_gamer:game', game_id=game.id)

    context = {'game':game, 'form':form}
    return render(request, 'board_gamer/edit_game.html', context)