from django import template
register = template.Library()
from pathlib import Path

#создание тега
@register.simple_tag  #это декоратор, превращает функцию в кастомный шаблонный тег
def full_path(file_name):
    #full_path_to_file = Path(__file__).parent.joinpath(file_name)
    return f'media/{file_name}'

#создание фильтра
@register.filter  #это декоратор, превращает функцию в кастомный шаблонный фильтр
def full_path(path):
    return f'media/{path}'

