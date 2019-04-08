from django.db import models
from django.contrib.auth.models import UserManager

class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    teacher = models.ManyToManyField(Teacher, related_name='students')
    group = models.CharField(max_length=10, verbose_name='Класс')

    # objects = UserManager()

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
