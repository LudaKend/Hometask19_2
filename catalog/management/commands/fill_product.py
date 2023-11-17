from django.core.management import BaseCommand
from pathlib import Path
import json
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Product.truncate_table_restart_id()
        list_products = self.load_from_json()

        for item in list_products:
            #сначала пришлось вытянуть по primary key значение категории из таблицы Category
            pk = item['fields']['category']
            print(pk)
            category = Category.objects.get(pk=pk)

    # образец для единичного ввода:
    #     list_products = {
    #   "name": "молоко", "description": "test",
    #   "category": category
    # }

    #         print(category)          # для отладки
    #         print(item)              # для отладки

            #фикстуру сформировала путем выгрузки из БД в json, в ней есть лишняя информация, беру только fields
            products_create = item['fields']
            # print(products_create)   # для отладки

            # поле 'category' является foreign key, поэтому django позволяет создать запись в таблице product только,
            # если подставить значение, которое вытащила из справочника Category,
            # например: <Category: 2, Молочные продукты, молоко, сыры, сметана, йогурты, творог>
            products_create['category'] = category
            # print(products_create)   # для отладки

            #создаем запись в таблице:
            Product.objects.create(**products_create)



        # пакетный вариант - не работает, потому что category должен быть объектом класса Category
        # нужно доработать!!!

        # products_for_create = []
        # for product in list_products:
        #     products_for_create.append(Product(**product['fields']))
        #     print(products_for_create)  # для отладки
        #     Product.objects.bulk_create(products_for_create)


    def load_from_json(self):
        '''Загружает в список записи продуктов из файла json'''
        json_path = Path(__file__).parent.joinpath('fixtura_product.json')
        print(json_path)  #для отладки
        with open(json_path, encoding='utf-8') as file:
            product_json = json.loads(file.read())
        return product_json
