from django.contrib import admin
from cart.models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['user', 'create']


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):

    list_display = ['user',  'items']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['user', 'name', 'telephon', 'price', 'order_date']






