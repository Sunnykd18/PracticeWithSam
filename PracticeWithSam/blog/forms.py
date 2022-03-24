from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Blog, BlogCategory


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'content', 'blog_categories']