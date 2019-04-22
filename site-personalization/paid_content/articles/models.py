from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    vip = models.BooleanField(verbose_name='Платный доступ')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название статьи')
    thematic = models.CharField(max_length=256, verbose_name='Тема статьи')
    text = models.TextField(verbose_name='Содержание статьи')
    paid = models.BooleanField(verbose_name='Платная статья')

    def __str__(self):
        return self.title


