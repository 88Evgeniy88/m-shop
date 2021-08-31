from PIL import Image
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import  ModelForm

from .models import *



class bookAdminForm(ModelForm):

    MIN_RES = (200, 200)


    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = self.MIN_RES
        if img.height < min_height or img.width < min_width:
            raise ValidationError('разрещение изображения меньше допустимого')
        return image



@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    form = bookAdminForm
    list_display = ('category', 'title', 'price', 'items', 'timeupdate')
    list_editable = ('price', 'items')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    form = bookAdminForm
    list_display = ('category', 'title', 'price', 'items', 'timeupdate')
    list_editable = ('price', 'items')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MuzCenter)
class MuzCenterAdmin(admin.ModelAdmin):
    form = bookAdminForm
    list_display = ('category', 'title', 'price', 'items', 'timeupdate')
    list_editable = ('price', 'items')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Refrigerator)
class RefrigeratorAdmin(admin.ModelAdmin):
    form = bookAdminForm
    list_display = ('category', 'title', 'price', 'items', 'timeupdate')
    list_editable = ('price', 'items')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}



