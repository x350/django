from django.core.management.base import BaseCommand
from django.conf import settings
from books.models import Book
import os
import json

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'fixtures/books.json')
        with open(file_path) as js_file:
            books = json.load(js_file)
            for item in books:
                Book.objects.create(name=item['fields']['name'].encode('cp1251').decode(),
                                    author=item['fields']['author'].encode('cp1251').decode(),
                                    pub_date=item['fields']['pub_date'])
