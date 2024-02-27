from django import forms
from .models import Product, Order
from django.core import validators


class AddProduct(forms.Form):

    name = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    description = forms.CharField(
        label='Product Description',
        widget=forms.Textarea,
        validators=[validators.RegexValidator(
            regex=r'new',
            message='Field must contain word "new"'
        )]
    )


class CreateOrderForm(forms.Form):
    class Meta:
        model = Order
        fields = ['delivery_address', 'promo_code', 'products']

    delivery_address = forms.CharField(max_length=30)
    promo_code = forms.CharField(max_length=20)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)
