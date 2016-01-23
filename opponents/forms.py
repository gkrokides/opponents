from django import forms

from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('player_1', 'player_2', 'sport',)

