from django.views.generic import ListView

from .models import Student, Teacher


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    def get_queryset(self):
        return self.model.objects.all().prefetch_related('teacher').values('name', 'teacher__name', 'teacher__subject')
