# Generated by Django 4.2.7 on 2024-01-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_key',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Ключ'),
        ),
    ]
