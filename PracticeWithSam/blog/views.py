from django.shortcuts import render, redirect
from .models import Blog,BlogCategory
from blog.forms import CreateBlogForm

def blog_list(request):
    context ={
        'objects': Blog.objects.all(),
    }
    return render(request, 'blog/blog_list.html', context=context)

def blog_detail(request, blog_id):
    context ={
        'blog':Blog.objects.get(id=blog_id),
    }
    return render(request, 'blog/blog_detail.html', context=context)


def create_blog(request):
    context ={}
    if request.method == 'POST':
        form = CreateBlogForm(request.POST or None)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_list')
    else:
        form=CreateBlogForm()
        context= {
            'createblog_form': form
        }
    return render(request, 'blog/create_blog.html', context=context)

def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        update_blog = CreateBlogForm(request.POST or None, instance=blog)
        if update_blog.is_valid():
            blog_ = update_blog.save(commit= False)
            blog_ = blog.save()
            return redirect('blog_list')

    form=CreateBlogForm(instance=blog)
    context = {
        'form':form,
    }
    return render(request, 'blog/update_blog.html', context=context)

def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if blog:
        blog.delete()

    return redirect('blog_list')