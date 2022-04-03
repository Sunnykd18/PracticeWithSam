from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog-details/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('update-blog/<int:blog_id>', views.update_blog, name='update_blog'),
    path('delete-blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('blog_by_category/<int:category_id>', views.blog_by_category, name='blog_by_category'),
    path('user_bloglist/', views.user_bloglist, name='user_bloglist'),
    path('create-save-post/', views.create_save_post, name='create_save_post'),

]
