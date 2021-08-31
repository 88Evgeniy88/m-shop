import csv

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from mainapp.models import Product
from .forms import OrderField
from .models import *


@login_required
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        cart = ' ваша корзина пуста '
    return render(request, 'cart/cart.html',  {'cart': cart})


@login_required
def add_to_card (request, slug, class_name):

    user = request.user
    cart, i = Cart.objects.get_or_create(user=request.user)
    content_type = ContentType.objects.get(model=class_name.lower())
    content_object = content_type.model_class().objects.get(slug=slug)
    cart_product, i = CartProduct.objects.get_or_create(
        user=user, cart=cart, content_type=content_type, object_id=content_object.id,  final_price=content_object.price)

    cart.products.add(cart_product)
    price = CartProduct.objects.filter(user=request.user).aggregate(Sum('final_price'))
    cart.final_price = price['final_price__sum']
    cart.save()
    return HttpResponseRedirect('/new/cart/')


@login_required
def remove_cart(request, pk):

    CartProduct.objects.filter(user=request.user, pk=pk).delete()
    cart = Cart.objects.get(user=request.user)
    price = CartProduct.objects.filter(user=request.user).aggregate(Sum('final_price'))
    cart.final_price = price['final_price__sum']
    cart.save()
    return HttpResponseRedirect('/new/cart/')


@login_required
def items_cart(request, pk):

    i = CartProduct.objects.get(user=request.user, pk=pk)
    price = i.final_price / i.items
    # обновляем итоговую цену товарной позиции по заданному количеству
    i.items = int(request.POST.get('items'))
    i.final_price = price * i.items
    i.save()
    # обновляем общую стоимость
    cart = Cart.objects.get(user=request.user)
    price = CartProduct.objects.filter(user=request.user).aggregate(Sum('final_price'))
    cart.final_price = price['final_price__sum']
    cart.save()
    return HttpResponseRedirect('/new/cart/')


@login_required
def order(request, pk):
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        cart = 'ваша корзина пуста'

    form = OrderField()
    if request.method == 'POST':
        form = OrderField(request.POST)
        user = request.user
        cart = Cart.objects.get(pk=pk, user=user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = user
            new_order.cart = cart
            new_order.price = cart.final_price
            new_order.save()
            pk = new_order.pk
            return HttpResponseRedirect('list/{}'.format(pk))
    return render(request, 'cart/order.html', {'form': form, 'cart': cart})


@login_required
def pyment(request):
    data = Order.objects.filter(user=request.user).order_by('-pk')

    return render(request, 'cart/pyment.html', {'data': data})


@login_required
def list_order(request, pk):
    a = Order.objects.get(pk=pk, user=request.user)

    # изменение остатков товара в базе
    for item in a.cart.products.all():
        seek_name_model = str(item.content_object).split()
        name_model = seek_name_model[0].lower()
        id_model = item.object_id

        content_type = ContentType.objects.get(model=name_model)
        object_mod = content_type.model_class().objects.get(pk=id_model)

        # запись заказа
        # write_item = item.items
        # write_categ = name_model
        # write = object_mod.title

        # изменение остатков в найденной строке
        object_mod.items = object_mod.items - item.items
        object_mod.save()


    cart = Cart.objects.get(user=request.user)
    cart.delete()

    messages.add_message(request, messages.INFO, 'Заказ успешно добавлен')
    return HttpResponseRedirect('/')



