from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    # здесь картинки товаров, а не то,что пользователь загрузил, поэтому путь такой указала...
    product_image = models.ImageField(upload_to='static/images/', verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    data_create = models.DateField(verbose_name='дата создания')
    data_change = models.DateField(verbose_name='дата изменения')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.name}, {self.category}, {self.price}'

    class Meta:
        #ordering = ('name')
        verbose_name = 'Продукт'  # для наименования одного объекта
        verbose_name_plural = 'Продукты'  # для наименования набора объектов

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    #created_at = models.CharField(max_length=10, verbose_name='Новое поле')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'  #для наименования одного объекта
        verbose_name_plural = 'категории' #для наименования набора объектов
        #ordering = ('name')
