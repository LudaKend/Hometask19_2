from django.db import connection
from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    # здесь картинки товаров, а не то,что пользователь загрузил, поэтому путь такой указала...
    product_image = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена', default=0)
    data_create = models.DateField(verbose_name='дата создания', auto_now_add=True)
    data_change = models.DateField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.name}, {self.description}, {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')


    def __str__(self):
        return f'{self.id}, {self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=100, verbose_name='Номер версии')
    version_name = models.TextField(verbose_name='Название версии', **NULLABLE)
    is_active = models.BooleanField(verbose_name='активная версия', default=False)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.product}, {self.version_number}, {self.is_active}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
