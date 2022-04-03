from django.shortcuts import render, redirect
from .models import Blog, BlogCategory, SavePost
from blog.forms import CreateBlogForm, CreateSavePostForm
from django.core.exceptions import ObjectDoesNotExist


def blog_list(request):
    context = {
        'objects': Blog.objects.all(),
        'categories': BlogCategory.objects.all(),
    }
    return render(request, 'blog/blog_list.html', context=context)


def blog_detail(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id),
    }
    return render(request, 'blog/blog_detail.html', context=context)


def create_blog(request):
    context = {}
    if request.method == 'POST':
        form = CreateBlogForm(request.POST or None)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_list')
    else:
        form = CreateBlogForm()
        context = {
            'createblog_form': form
        }
    return render(request, 'blog/create_blog.html', context=context)


def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        update_blog = CreateBlogForm(request.POST or None, instance=blog)
        if update_blog.is_valid():
            blog_ = update_blog.save(commit=False)
            blog_ = blog.save()
            return redirect('blog_list')

    form = CreateBlogForm(instance=blog)
    context = {
        'form': form,
    }
    return render(request, 'blog/update_blog.html', context=context)


def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if blog:
        blog.delete()

    return redirect('blog_list')


def blog_by_category(request, category_id):
    context = {
        'objects': Blog.objects.filter(blog_categories__in=[category_id]),
        'blog_categories': BlogCategory.objects.all(),
        'category': BlogCategory.objects.get(id=category_id),
    }
    if len(context['objects']) == 0:
        context['message'] = "No blog of " + str(context['category']) + "category."
    else:
        context['message'] = "Blog with " + str(context['category']) + "category."
    return render(request, 'blog/blog_list.html', context=context)


def create_save_post(request):
    context = {}
    if request.method == 'POST':
        form = CreateSavePostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = CreateSavePostForm()
        context = {
            'create_save_post': form
        }
    return render(request, 'blog/create_save_post.html', context=context)


def user_bloglist(request):
    context = {
        'user_bloglist': SavePost.objects.filter(user=request.user)
    }
    return render(request, 'blog/user_bloglist.html', context=context)


