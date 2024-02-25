from django import forms
from .models import Product


class AddProduct(forms.Form):

    name = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    description = forms.CharField(label='Product Description', widget=forms.Textarea)


class CreateOrderForm(forms.Form):

    delivery_address = forms.CharField(max_length=30)
    promo_code = forms.CharField(max_length=20)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
