from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.ModelForm):
    # name = forms.CharField(label='Введите имя:')
    # password = forms.CharField(label='Ввидите пароль: ')
    pass

    class Meta:
        model = User
        fields = ('username', 'password',)
