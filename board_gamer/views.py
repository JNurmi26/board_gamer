from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Game
from .forms import GameForm

# Create your views here.
def index(request):
    """The home page for Board Gamer"""
    return render(request, 'board_gamer/index.html')

@login_required
def games(request):
    """Show all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_gamer/games.html', context)

@login_required
def game(request, game_id):
    """Show a single game"""
    game = Game.objects.get(id=game_id)
    context = {'game':game}
    return render(request, 'board_gamer/game.html', context)

@login_required
def new_game(request):
    """Add a new game"""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = GameForm()
    else:
        # POST data submitted, process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('board_gamer:games')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_gamer/new_game.html', context)

@login_required
def edit_game(request, game_id):
    """Edit an existing game."""
    game = Game.objects.get(id=game_id)
    if game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request, pre-fill form with current game info.
        form = GameForm(instance=game)
    else:
        # POST data submitted, process data.
        form = GameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('board_gamer:game', game_id=game.id)

    context = {'game':game, 'form':form}
    return render(request, 'board_gamer/edit_game.html', context)