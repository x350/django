# Generated by Django 2.1.1 on 2019-04-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190423_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='continue_attempt',
            field=models.BooleanField(default=False, verbose_name='Игра продолжается'),
        ),
    ]
