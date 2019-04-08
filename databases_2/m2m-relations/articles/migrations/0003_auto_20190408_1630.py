# Generated by Django 2.1.1 on 2019-04-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='name_tag',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='articles.Tags'),
        ),
    ]
