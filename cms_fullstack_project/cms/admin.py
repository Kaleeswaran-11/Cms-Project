from django.contrib import admin
from .models import Post, Category, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','status','created_at')
    list_filter=('status','category')
    search_fields=('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','role')
