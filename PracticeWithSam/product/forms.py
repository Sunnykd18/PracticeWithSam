from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from product.models import Product, Category
from users.models import Seller


class CreateProductForm(forms.ModelForm):
    # product_name = forms.CharField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'categories']


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

