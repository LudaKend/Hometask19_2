from django.conf import settings
from django.core.cache import cache
from catalog.models import Category

def get_category_from_cache():
    '''считывает все категории из кеша,если кеш пуст,то заполняет его из БД,если кеш выключен,то берет из БД'''
    if settings.CACHE_ENABLED:
        key = f'categories'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
    else:
        categories = Category.objects.all()
    return categories
