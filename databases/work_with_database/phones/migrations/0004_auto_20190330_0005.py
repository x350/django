# Generated by Django 2.1.1 on 2019-03-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20190330_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.FileField(upload_to='phones'),
        ),
    ]