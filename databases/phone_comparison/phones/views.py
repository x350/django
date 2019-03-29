from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    phone = Phone.objects.all()
    context = {'phone': phone}

    return render(request, 'catalog.html', context)
