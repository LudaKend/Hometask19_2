from django.core.management import BaseCommand
from pathlib import Path
import json
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        '''удаляет все записи из таблицы Category и заполняет таблицу записями из json-файла'''
        Category.objects.all().delete()
        Category.truncate_table_restart_id()
        list_category = self.load_from_json()
        print(list_category)

        # for item in list_category:
        #     print(item)
        #     Category.objects.create(**item)
        category_for_create = []
        for item in list_category:
            category_for_create.append(Category(**item['fields']))

        print(category_for_create)  #для отладки
        Category.objects.bulk_create(category_for_create)


    def load_from_json(self):
        '''Загружает в список записи категорий из файла json'''
        json_path = Path(__file__).parent.joinpath('fixtura_category.json')
        print(json_path)  #для отладки
        with open(json_path, encoding='utf-8') as file:
            category_json = json.loads(file.read())
        return category_json

