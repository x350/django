from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

    def review_count(self):
        return Review.objects.filter(car=self).count()
    review_count.short_description = 'REVIEW COUNT'



class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

