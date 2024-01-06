from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Blog_post(models.Model):
    head = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Слаг')
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='Превью')
    data_create = models.DateField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликован', default=False)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.head}, {self.slug}, {self.is_published}, {self.views_count}'

    class Meta:
        verbose_name = 'Пост'  # для наименования одного объекта
        verbose_name_plural = 'Посты в блоге'  # для наименования набора объектов
