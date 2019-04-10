from django.views.generic import ListView

from .models import Student, Teacher


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    def get_queryset(self):
        queryset = self.model.objects.all()
        print(queryset.values())
        return queryset




# class TeacherListView(ListView):
#     model = Teacher
#     def get_queryset(self):
#         queryset = self.model.objects.students
#         print(queryset.values())
#         return queryset