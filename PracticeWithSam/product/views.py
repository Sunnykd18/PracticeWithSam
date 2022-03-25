from django.shortcuts import render, redirect
from .models import Product, Category
from product.forms import CreateProductForm, CreateCategoryForm


def product_list(request, **kwargs):
    context = {
        'objects': Product.objects.all(),
        'categories': Category.objects.all(),
    }
    # result = []
    # for pro in Product.objects.all():
    #     cat_1 = [ids['id'] for ids in pro.categories.all().values('id')]
    #     print(cat_1, "CAT_!")
    #     if 4 in cat_1:
    #         result.append(pro)
    # print(result, "RESUTL")
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
            product = form.save()
            # product.seller =
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
        update_form = CreateProductForm(request.POST or None, instance=product)
        if update_form.is_valid():
            product_ = update_form.save(commit=False)
            product_.save()
            return redirect('product_list')
    form = CreateProductForm(instance=product)
    context = {
        "form": form,
    }
    return render(request, 'product/update_product.html', context=context)


def update_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)

    if request.method == 'POST':
        update_form = CreateCategoryForm(request.POST or None, instance=cat)
        if update_form.is_valid():
            cat_ = update_form.save(commit=False)
            cat_.save()
            return redirect('product_list')
    form = CreateCategoryForm(instance=cat)
    context = {
        "form": form,
    }
    return render(request, 'product/update_category.html', context=context)


def delete_product(request, pro_id):
    product = Product.objects.get(id=pro_id)

    if request.method == 'POST':
        update_form = CreateProductForm(request.POST or None, instance=product)
        if update_form:
            product.delete()
            return redirect('product_list')
        context = {
            "error": "this is error",
        }
    form = CreateProductForm(instance=product)
    context = {
        "form": form
    }
    return render(request, 'product/delete_product.html', context=context)


def product_by_category(request, category_id):
    context = {
        'objects': Product.objects.filter(categories__in=[category_id]),
        'categories': Category.objects.all(),
        'category': Category.objects.get(id=category_id),

    }
    if len(context['objects']) == 0:
        context['messages'] = "No product of this category"
    else:
        context['messages'] = "Product with category"
    return render(request, 'product/product_list.html', context=context)
