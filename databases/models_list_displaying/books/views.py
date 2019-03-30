from django.views import generic
from django.conf import settings
import os
import json
from .models import Book

class BookListView(generic.ListView):
    model = Book



    def get_context_data(self, **kwargs):
        context = {}
        file_path = os.path.join(settings.BASE_DIR, 'fixtures/books.json')
        with open(file_path, encoding='cp1251') as js_file:
            books = json.load(js_file)
            print(books)
