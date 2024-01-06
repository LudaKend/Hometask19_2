from django.contrib import admin
from blog.models import Blog_post


@admin.register(Blog_post)
class Blog_postAdmin(admin.ModelAdmin):
    list_display = ('head', 'slug', 'content', 'data_create', 'is_published', 'views_count')

    search_fields = ('head', 'slug')
