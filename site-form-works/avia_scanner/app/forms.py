from django import forms
from django.forms.widgets import SelectDateWidget
from django.urls import reverse_lazy


from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    from_city = forms.CharField(label='Город отправления', widget=AjaxInputWidget(url=reverse_lazy('lookup')))
    to_city = forms.ModelChoiceField(queryset=City.objects.all(),
        empty_label='----------', label='Город прибытия')
    date = forms.DateField(widget=SelectDateWidget)

