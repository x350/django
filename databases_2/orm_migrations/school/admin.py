from django.contrib import admin

from .models import Student, Teacher


class StudentInLine(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        StudentInLine,
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        StudentInLine,
    ]

