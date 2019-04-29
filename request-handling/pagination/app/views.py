from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
import csv

ITEMS_ON_PAGE = 10


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        paginator = Paginator(list(reader), ITEMS_ON_PAGE)
        get_page = request.GET.get('page')
        if not get_page:
            page = 1
        else:
            page = int(get_page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return render_to_response('index.html', {'items': items})
