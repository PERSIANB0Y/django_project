from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=0, max_digits=9)
    img = models.ImageField(upload_to='migrations/images/')

    def __str__(self):
        return self.name, self.price, self.img


class Category(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name, self.items
