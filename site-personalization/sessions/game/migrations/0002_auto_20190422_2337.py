# Generated by Django 2.1.1 on 2019-04-22 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='gamer',
            new_name='game_id',
        ),
    ]
