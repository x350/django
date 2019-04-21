from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return self.brand

    def review_count(self):
        return Review.objects.filter(car=self).count()
    review_count.short_description = 'Количество обзоров'

    brand.admin_order_field = '-id'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField()

    car.admin_order_field = '-id'

    def __str__(self):
        return str(self.car) + ' ' + self.title

