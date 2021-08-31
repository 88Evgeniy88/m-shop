from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('<str:class_name>', product, name='product'),
    path('detail/<str:slug>/<str:class_name>', detal, name='detail')

]