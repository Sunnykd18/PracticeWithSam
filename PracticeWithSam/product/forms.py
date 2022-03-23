from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from product.models import Product, Category
from users.models import Seller


class CreateProductForm(forms.ModelForm):
    # product_name = forms.CharField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'seller', 'categories']


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'categories']

    def save(self, commit=True):
        product = self.instance
        product.name = self.cleaned_data['name']
        product.price = self.cleaned_data['price']
        product.categories = self.cleaned_data['categories']

        if commit:
            product.save()
        return product


