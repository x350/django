from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    # def get_queryset(self):
    #     queryset = self.model.objects.prefetch_related('teacher')
    #     print(queryset.values())
    #     return queryset