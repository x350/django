# Generated by Django 2.1.1 on 2019-04-09 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20190409_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teachers',
            new_name='teacher',
        ),
    ]