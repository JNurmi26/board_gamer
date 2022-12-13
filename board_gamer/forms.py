from django import forms

from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['text', 'description']
        labels = {'text':''}
        

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['is_borrowed',]
