from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog-details/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('update-blog/<int:blog_id>', views.update_blog, name='update_blog'),
    path('delete-blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('blog_by_category/<int:category_id>', views.blog_by_category, name='blog_by_category'),
    path('create-save-post/<int:blog_id>', views.create_save_post, name='create_save_post'),
    path('add-to-save-post/<int:blog_id>/<int:save_post_id>', views.create_save_post, name='create_save_post'),
    path('saved-post-list/<int:blog_id>', views.saved_post_list, name='saved_post_list'),
]
