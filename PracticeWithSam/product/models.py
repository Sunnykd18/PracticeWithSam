from django.db import models
from users.models import Seller, Buyer


class Product(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    price = models.IntegerField(default=0)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE ,blank=True,null=True)
    categories = models.ManyToManyField('Category')
    image = models.ImageField(default='default.jpg', upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();


class Category(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.name
