from django.shortcuts import render
from django.views import View


# Create your views here.
from .models import Path, Table
import csv


CSV_FILENAME = 'phones.csv'
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


class TableView(View):
    def get(self, request):
        for item in COLUMNS:
            Table.objects.create(name=item['name'], width=item['width'])
        #
        #
        # Path.set_path(Path, CSV_FILENAME)
        print('=====', Path.get_path(Path))
        # if not path_csv:
        #     path_csv = CSV_FILENAME
        with open(CSV_FILENAME, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)

            result = render(request, 'table.html', {'columns': COLUMNS, 'table': table, 'csv_file': CSV_FILENAME})
        return result

