from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog-details', views.blog_detail, name='blog_detail'),
    path('create-blog/<int:blog_id>', views.create_blog, name='create_blog'),
    path('update-blog/<int:blog_id', views.update_blog, name='update_blog'),
    path('delete-blog/<int:blog_id', views.delete_blog, name='delete_blog'),

]
