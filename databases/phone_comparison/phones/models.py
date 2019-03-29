from django.db import models

# Create your models here.

class Phone(models.Model):
    brend = models.CharField(max_length=20)
    model_phone = models.CharField(max_length=20)
    os_phone = models.CharField(max_length=10)
    display_size = models.DecimalField(max_digits=2, decimal_places=1)
    storage_memory = models.IntegerField()
    fm_tuner = models.BooleanField()
    nfc = models.BooleanField()
    cpu_frequency = models.FloatField()
    color = models.CharField(max_length=15)
    camera_mp = models.FloatField()
