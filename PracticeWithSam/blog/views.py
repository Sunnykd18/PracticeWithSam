from django.shortcuts import render, redirect
from .models import Blog, BlogCategory, SavePost
from blog.forms import CreateBlogForm, CreateSavePostForm
from django.core.exceptions import ObjectDoesNotExist


def blog_list(request):
    print(request, "Request")
    print(request.user, "User")
    print(request.user.username, "Username")
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


def create_save_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = CreateSavePostForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save()
            form_obj.blog.add(blog)

            return redirect('blog_list')
    else:
        form = CreateSavePostForm()
        context = {
            'create_save_post': form
        }
    return render(request, 'blog/create_save_post.html', context=context)


def add_to_save_post(request, blog_id, save_post_id):
    if not request.user.is_authenticated():
        return redirect("login")
    new_blog = Blog.objects.get(id=blog_id)
    save_post = SavePost.objects.get(id=save_post_id)
    current_user = User.objects.get(username=request.user.username)
    if save_post:
        save_post.blog.add(new_blog)
        return redirect('blog_list')


def saved_post_list(request, blog_id):
    context = {
            'saved_post': SavePost.objects.all(),
            'blog': Blog.objects.get(id=blog_id),
            'categories': BlogCategory.objects.all(),
    }
    # if context['saved_post']:
    #     context['saved_postlist'] = context['saved_post']
    # else:
    #     return redirect('blog_list')

    return render(request, 'blog/saved_post.html', context=context)
def saved_post_list_by_name(request, save_post_id):
    context = {
        'saved_post': SavePost.objects.get(id=save_post_id),
        # 'blog': Blog.objects.get(id=blog_id),
        # 'categories': BlogCategory.objects.all(),
    }
    return render(request, 'blog/saved_post_list_by_name.html', context=context)
