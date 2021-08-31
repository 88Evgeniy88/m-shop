from django import forms

from .models import Order


class OrderField(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'telephon', 'address', 'buying_type')



