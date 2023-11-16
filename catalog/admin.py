from django.contrib import admin

# Register your models here.

from catalog.models import Product, Category
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')

    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
