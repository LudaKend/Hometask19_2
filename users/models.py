from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватар')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    country = models.CharField(max_length=50, verbose_name='Страна')
    verification_key = models.CharField(max_length=4, verbose_name='Ключ', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.email}, {self.is_active}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
