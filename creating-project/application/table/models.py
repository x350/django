from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    width = models.PositiveIntegerField()
    # number_field = models.PositiveSmallIntegerField()
    number_field = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Path(models.Model):
    path = models.CharField(max_length=1024, verbose_name='Путь к CSV файлу', primary_key=True)

    def get_path(self):
        if self.path:
            return self.path
        else:
            return 'Хрен'

    # def set_path(self, *args, **kwargs):
        # super(Path, self).save(*args, **kwargs)

    def set_path(self, path):
        if self.path:
            super(Path, self).delete(path)
        super(Path, self).save(path)

    def __str__(self):
        return self.path




