from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Category, PostCategory
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostCategory)