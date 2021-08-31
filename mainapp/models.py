from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__.meta.model_name
    return reverse(viewname, kwargs={'ct_model' : ct_model, 'slug': obj.slug})


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    name = models.CharField('Имя категории', max_length=100)
    slug = models.SlugField('Слаг', unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=255)
    slug = models.SlugField('Слаг', unique=True)
    image = models.ImageField('Изображение')
    timeupdate = models.DateTimeField('Дата обновления', auto_now=True)
    description = models.TextField('Описание', null=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    items = models.PositiveIntegerField('Остатки', default=0)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug, 'class_name': self.__class__.__name__})

    def get_add_card(self):
        return reverse('add-to-cart', kwargs={'slug': self.slug, 'class_name': self.__class__.__name__})



class Notebook(Product):

    class Meta:
        verbose_name_plural = 'ноутбуки'
        verbose_name = ' ноутбук'

    diagonal = models.CharField("Диагональ", max_length=20)
    hdd = models.CharField('Объем жесткого диска', max_length=100 , null=True)
    processopr_freq = models.CharField('Частота процессора', max_length=100)
    ram = models.CharField('Оперативная память', max_length=100)
    time_work = models.CharField('Время работы', max_length=20)




class TV(Product):
    class Meta:
        verbose_name_plural = 'телевизоры'
        verbose_name = 'телевизор'

    diagonal = models.CharField("Диагональ", max_length=20)
    resolution = models.CharField('Разрешение', max_length=100)
    smart_TV = models.BooleanField("Smart TV", default=False)
    os = models.CharField('Операционная система ', max_length=100, blank=True)
    hdmi = models.CharField('Количество HDMI', max_length=10)




class Refrigerator(Product):

    class Meta:
        verbose_name_plural = 'холодильники'
        verbose_name = 'холодильник'

    volume = models.CharField('Общий полезный объем', max_length=20)
    height = models.CharField('Высота', max_length=20)
    width = models.CharField('Ширина', max_length=20)
    frozen_c = models.SmallIntegerField('Количество отделеий в морозильной камере')
    no_frost = models.BooleanField('Система No Frost', default=False)




class MuzCenter(Product):
    class Meta:
        verbose_name_plural = 'Музыкальные центры'
        verbose_name = 'Музыкальный центр'

    volume_power = models.CharField('Выходная мощность усилителя', max_length=10)
    type = models.CharField('Тип акустики', max_length=10)
    karaoke = models.BooleanField('Караоке', default=False)




