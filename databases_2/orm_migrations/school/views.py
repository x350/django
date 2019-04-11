from django.views.generic import ListView

from .models import Student, Teacher


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    def get_queryset(self):
        # set = self.model.objects.all()
        # queryset = {student.group: {student.teacher.all()} for student in self.model.objects.all()}
        queryset = self.model.objects.all().prefetch_related('teacher').values('name', 'teacher__name', 'teacher__subject')

        print(queryset)
        return queryset




# class TeacherListView(ListView):
#     model = Teacher
#     def get_queryset(self):
#         queryset = self.model.objects.students
#         print(queryset.values())
#         return queryset