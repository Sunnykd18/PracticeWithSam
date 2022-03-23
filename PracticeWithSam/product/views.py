from django.shortcuts import render, redirect
from .models import Product
from product.forms import CreateProductForm, CreateCategoryForm, UpdateProductForm


def product_list(request):
    context = {
        'objects': Product.objects.all(),
    }
    return render(request, 'product/product_list.html', context=context)


def product_detail(request, pro_id):
    product = Product.objects.get(id=pro_id)
    context = {
        'obj': product,
    }
    return render(request, 'product/product_detail.html', context=context)


def create_product(request):
    context = {
    }
    if request.method == "POST":
        form = CreateProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CreateProductForm()
        context['product'] = Product.objects.all()
        context['createproduct_form'] = form
    return render(request, 'product/create_product.html', context=context)


def create_category(request):
    context = {}
    if request.method == "POST":
        form = CreateCategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CreateCategoryForm()
        context['createcategory_form'] = form
    return render(request, 'product/create_category.html', context=context)


def update_product(request, pro_id):
    product = Product.objects.get(id=pro_id)

    if request.method == 'POST':
        update_form = UpdateProductForm(request.POST or None, instance=product)
        if update_form.is_valid():
            product_ = update_form.save(commit=False)
            product_.save()
            product = product_
            return redirect('product_list', id=pro_id)
    form = UpdateProductForm(
        initial={
            "name": product.name,
            "price": product.price,
            "categories": product.categories,
        }
    )
    context = {
        "form": form,
        "product": product,
    }
    return render(request, 'product/update_product.html', context=context)
