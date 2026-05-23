from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)   # название
    brand = models.CharField(max_length=50)   # бренд
    price = models.IntegerField()              # цена
    ram = models.IntegerField()                # оперативная память (ГБ)
    
    def __str__(self):
        return self.name
# Create your models here.
