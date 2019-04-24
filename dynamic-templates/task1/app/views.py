from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import os, csv


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        context = {}
        file_path = os.path.join(settings.BASE_DIR, 'inflation_russia.csv')
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            context['head'] = next(reader)
            context['data'] = []
            for row in reader:
                context['data'].append(row)
        return render(request, self.template_name, context)

