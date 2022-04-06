from django.db import models
from users.models import Seller, Buyer
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    price = models.IntegerField(default=0)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)
    categories = models.ManyToManyField('Category')
    image = models.ImageField(default='default.jpg', upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)


class Category(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    product = models.ManyToManyField(Product)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist"

