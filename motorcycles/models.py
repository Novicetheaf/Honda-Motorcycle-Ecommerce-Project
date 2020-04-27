from django.db import models


# Create your models here.
class Motorcycle(models.Model):
    name = models.CharField(max_length=199, default='')
    engine = models.IntegerField(default='')
    weight = models.IntegerField(default='')
    description = models.TextField(max_length=350)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
