from django.contrib import admin

# Register your models here.
from blog.models import Blog_post
#admin.site.register(Product)

@admin.register(Blog_post)
class Blog_postAdmin(admin.ModelAdmin):
    list_display = ('head', 'slug', 'content', 'data_create', 'is_published', 'views_count')

    search_fields = ('head', 'slug')
