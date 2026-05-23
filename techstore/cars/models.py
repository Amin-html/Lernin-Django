from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)   # название
    brand = models.CharField(max_length=50)   # бренд
    power = models.IntegerField()              # мощность (л.с.)
    price = models.IntegerField()              # цена
    
    def __str__(self):
        return self.name

# Create your models here.
