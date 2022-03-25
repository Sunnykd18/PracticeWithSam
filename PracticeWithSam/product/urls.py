from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pro_id>', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_category/', views.create_category, name='create_category'),
    path('update-product/<int:pro_id>', views.update_product, name='update_product'),
    path('delete-product/<int:pro_id>', views.delete_product, name='delete_product'),
    path('update-category/<int:cat_id>', views.update_category, name='update_category'),
    path('product-by-categories/<int:category_id>', views.product_by_category, name='product_by_category')
]
