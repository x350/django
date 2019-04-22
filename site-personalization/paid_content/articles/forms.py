from django import forms
from .models import Profile

class InputName(forms.ModelForm):
    # text = forms.CharField(label="Ваше имя")

    class Meta:
        model = Profile
        fields = ('name',)