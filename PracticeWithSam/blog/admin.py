from django.contrib import admin
from .models import Blog, BlogCategory, SavePost


admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(SavePost)