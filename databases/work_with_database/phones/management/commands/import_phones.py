import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

from django.template.defaultfilters import slugify
import requests
# import tempfile
# from django.core import files
# from PIL import Image
# from io import BytesIO


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                Phone.objects.create(id=line[0], name=line[1], image=get_image(line[2], line[1]),
                                     price=line[3], release_date=line[4], lte_exists=line[5],
                                     slug=slugify(line[1]))

# import urllib.request
# def get_image(url):
#     return urllib.request.urlretrieve(url)[0]


def get_image(url, name):
    request = requests.get(url, stream=True)
    out = open('static/' + name + ".jpg", "wb")
    out.write(request.content)
    out.close()
    return name + ".jpg"




