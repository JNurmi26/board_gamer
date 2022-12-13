from django.contrib import admin

from .models import Game
from .models import Gamer

# Register your models here.
admin.site.register(Game),
admin.site.register(Gamer)