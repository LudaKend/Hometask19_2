# Generated by Django 4.2.7 on 2024-01-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_version_product_alter_version_version_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_name',
            field=models.TextField(blank=True, help_text='Образец заполнения: поступление 1.12.2023', null=True, verbose_name='Название версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.CharField(help_text='Образец заполнения: 1/2023', max_length=100, verbose_name='Номер версии'),
        ),
    ]