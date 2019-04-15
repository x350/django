import datetime
import time
import os

from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        context = super(FileList, self).get_context_data()
        context['files'] = []
        context['date'] = None

        if date is not None:
            context['date'] = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        files_path = os.path.join(settings.BASE_DIR, 'files')

        list_files = os.listdir(files_path)
        for item in list_files:
            ctime = time.localtime(os.stat(os.path.join(files_path, item)).st_ctime)
            mtime = time.localtime(os.stat(os.path.join(files_path, item)).st_mtime)

            file_dict = {}
            file_dict['name'] = item
            file_dict['ctime'] = datetime.datetime(ctime.tm_year, ctime.tm_mon, ctime.tm_mday, ctime.tm_hour, ctime.tm_min)
            file_dict['mtime'] = datetime.datetime(mtime.tm_year, mtime.tm_mon, mtime.tm_mday, mtime.tm_hour, mtime.tm_min)
            context['files'].append(file_dict)
        return context


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files_path = os.path.join(settings.BASE_DIR, 'files', name)
    content = ''
    if os.path.exists(files_path):
        with open(files_path) as f:
            content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': content, }
    )
