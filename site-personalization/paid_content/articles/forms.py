from django import forms
from .models import Profile
from django.contrib.auth.models import User

class InputName(forms.ModelForm):
    # text = forms.CharField(label="Ваше имя")

    class Meta:
        model = User
        fields = ('username', 'password')