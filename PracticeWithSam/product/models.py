from django.db import models
from users.models import Seller, Buyer

class Product(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=70,blank=True,null=True)

    def __str__(self):
        return self.name
