from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mainapp.models import *
from cart.models import *


def index(request):
    try:
        cart, st = Cart.objects.get_or_create(user=request.user)
    except:
        cart = None
    return render(request, 'mainapp/index.html', {'cart': cart})


def product(request, class_name):
    try:
        cart, st = Cart.objects.get_or_create(user=request.user)
    except:
        cart = None
    content_type = ContentType.objects.get(model=class_name)

    if request.GET.get('search'):
        get = request.GET.get('search')
        data = content_type.model_class().objects.filter(title__icontains=get)
    else:
        data = content_type.model_class().objects.all()
    try:
        name = data[0].category
    except:
        name = 'Товара нет в наличии'

    return render(request, 'mainapp/category.html', {'data': data,
                                                     'name': name,
                                                     'cart': cart})



def detal(request, slug, class_name):
    try:
        cart, st = Cart.objects.get_or_create(user=request.user)
    except:
        cart = None
    content_type = ContentType.objects.get(model=class_name.lower())
    item = content_type.model_class().objects.get(slug=slug)

    return render(request, 'mainapp/detailView.html', {'item': item, 'cart': cart})



