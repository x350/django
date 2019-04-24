from django import forms
from .models import Game

class InputNumber(forms.ModelForm):
    number = forms.IntegerField(max_value=10, min_value=0)

    class Meta:
        model = Game
        fields = ('number',)