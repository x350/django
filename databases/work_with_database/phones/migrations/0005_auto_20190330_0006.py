# Generated by Django 2.1.1 on 2019-03-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20190330_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to='phones'),
        ),
    ]
