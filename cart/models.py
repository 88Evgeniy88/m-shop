from django.db import models
from mainapp.models import *



class CartProduct(models.Model):
    class Meta:
        verbose_name = 'Хранилище'
        verbose_name_plural = 'Хранилище'

    user = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products', null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    items = models.PositiveSmallIntegerField('Количество', default=1)
    final_price = models.DecimalField('Итоговая цена',max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.pk)




class Cart(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    create = models.DateField('Дата создания', auto_now_add=True)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveSmallIntegerField('Общее количество', default=0)
    final_price = models.DecimalField('Итоговая цена', max_digits=9 , decimal_places=2, null=True, blank=True)



    def __str__(self):
        return str(self.pk)


class Order (models.Model):

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'


    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    name = models.CharField('Имя', max_length=20)
    telephon = models.CharField('Телефон', max_length=20)
    user = models.ForeignKey(User, verbose_name='Юзер', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField('Цена заказа', max_digits=9, decimal_places=2)
    buying_type = models.CharField('Тип заказа', max_length=30,
                                   choices=BUYING_TYPE_CHOICES,
                                   default=BUYING_TYPE_SELF
                                   )
    order_date = models.DateField('Дата создания заказа', auto_now=True)
    address = models.CharField('Адрес', max_length=100, null=True)

