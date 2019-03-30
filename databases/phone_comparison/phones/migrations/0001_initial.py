# Generated by Django 2.1.1 on 2019-03-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.TextField()),
                ('model_phone', models.TextField()),
                ('os_phone', models.TextField()),
                ('display_size', models.DecimalField(decimal_places=1, max_digits=2)),
                ('storage_memory', models.IntegerField()),
                ('fm_tuner', models.BooleanField()),
                ('nfc', models.BooleanField()),
                ('cpu_frequency', models.FloatField()),
                ('color', models.TextField()),
                ('camera_mp', models.FloatField()),
            ],
        ),
    ]