from django.core.management.base import BaseCommand
from school.models import Teacher, Student
from django.conf import settings
import json
import os

path = settings.BASE_DIR

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(path, 'school.json'), 'r') as r_file:
            data = json.load(r_file)
            for item in data:
                print(item)
                if item['model'] == 'school.teacher':
                    Teacher.objects.create(id=item['pk'], name=item['fields']['name'], subject=item['fields']['subject'])
                elif item['model'] == 'school.student':
                    teach_obg = Teacher.objects.filter(id=item['fields']['teacher'])
                    stud_obj = Student.objects.create(id=item['pk'], name=item['fields']['name'], group=item['fields']['group'])
                    stud_obj.teacher.set(teach_obg)






