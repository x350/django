from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from django.conf import settings
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    get_param = request.GET.get('page')
    if not get_param:
        get_param = 1
    else:
        get_param = int(get_param)

    bus_stop_list = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stop_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    prev_pg = get_param - 1
    next_pg = get_param + 1
    count_page = len(bus_stop_list) // 10 + 1

    context = {
        'bus_stations': bus_stop_list[get_param * 10 - 10: get_param * 10],
        'current_page': get_param,
    }

    if prev_pg < 1:
        context['prev_page_url'] = None
        context['next_page_url'] = 'bus_stations?page=' + str(next_pg)
    elif next_pg > count_page:
        context['prev_page_url'] = 'bus_stations?page=' + str(prev_pg)
        context['next_page_url'] = None
    else:
        context['prev_page_url'] = 'bus_stations?page=' + str(prev_pg)
        context['next_page_url'] = 'bus_stations?page=' + str(next_pg)

    return render_to_response('index.html', context)
