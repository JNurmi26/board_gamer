from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Board Gamer"""
    return render(request, 'board_gamer/index.html')