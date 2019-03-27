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
            reader = csv.DictReader(csvfile)
            context['data'] = []
            for row in reader:
                item = row.popitem()
                title = item[0].split(';')
                title[-1] = 'Всего'
                context['title'] = title

                temp = item[1].split(';')
                prepList = temp[:1]
                for i in temp[1:-1]:
                    if i.isdigit():
                        prepList.append(float(i))
                    else:
                        prepList.append(i)
                prepList.append(temp[-1])
                context['data'].append(prepList)
                break
            for row in reader:
                context['data'].append(readRow(row))

                # context['data'].append((float(item) for item in (row.popitem()[1]).split(';')))
        return render(request, self.template_name,
                      context)

def readRow(row):
    currentList = (row.popitem()[1]).split(';')
    prepList = currentList[:1]
    prepList += [float(item) for item in currentList[1:-1]]
    prepList.append(currentList[-1])
    return prepList
