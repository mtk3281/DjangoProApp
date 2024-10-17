from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'slug']
    list_filter = ['subtitle', 'created_at', 'author']
    search_fields = ['title', 'subtitle']
    raw_id_fields = ['author']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    # filter_horizontal = ['tags']  # Ensure it's a tuple


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display = ['name', 'email', 'post', 'created', 'active']
 list_filter = ['active', 'created', 'updated']
 search_fields = ['name', 'email', 'body']