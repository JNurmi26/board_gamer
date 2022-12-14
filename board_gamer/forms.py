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


class UserForm(forms.ModelForm): 
    username = forms.CharField(max_length=100, required=True)
    class Meta: 
        model = Gamer
        fields = ['username']
