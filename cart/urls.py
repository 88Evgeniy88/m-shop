from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cart, name='cart'),
    path('add-to-cart/<str:slug>/<str:class_name>', add_to_card, name='add-to-cart'),
    path('remove-cart/<int:pk>', remove_cart, name='remove-cart'),
    path('items-cart/<int:pk>', items_cart, name='items-cart'),
    path('order/<int:pk>', order, name='order'),
    path('order/list/<int:pk>', list_order, name='list-order'),
    path('order/pyment/', pyment, name='pyment')
]