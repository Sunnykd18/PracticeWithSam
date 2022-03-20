from django.db import models
from django.contrib.auth.models import User

class Buyer(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





