# Generated by Django 3.2.6 on 2021-08-27 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notebook',
            options={'verbose_name': ' ноутбук', 'verbose_name_plural': 'ноутбуки'},
        ),
        migrations.AlterModelOptions(
            name='tv',
            options={'verbose_name': 'телевизор', 'verbose_name_plural': 'телевизоры'},
        ),
    ]
