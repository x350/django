# Generated by Django 2.1.1 on 2019-03-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='brend',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='phone',
            name='color',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='phone',
            name='model_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='phone',
            name='os_phone',
            field=models.CharField(max_length=10),
        ),
    ]
