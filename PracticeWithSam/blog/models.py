from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    content = models.TextField(max_length=600, blank=True, null=True)
    blog_categories = models.ManyToManyField('BlogCategory')

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.name

