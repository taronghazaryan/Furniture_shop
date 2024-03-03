from django import forms
from .models import Product, Order
from django.core import validators

# long version for create Product
# class AddProduct(forms.Form):
#
#     name = forms.CharField(max_length=20)
#     price = forms.DecimalField(max_digits=6, decimal_places=2)
#     description = forms.CharField(
#         label='Product Description',
#         widget=forms.Textarea,
#         validators=[validators.RegexValidator(
#             regex=r'new',
#             message='Field must contain word "new"'
#         )]
#     )


# short version
class AddProduct(forms.ModelForm):
    class Meta:

        model = Product
        fields = ['name', 'price', 'description']

# long version to Create Order
# class CreateOrderForm(forms.Form):
#     class Meta:
#         model = Order
#         fields = ['delivery_address', 'promo_code', 'products']
#
#     delivery_address = forms.CharField(max_length=30)
#     promo_code = forms.CharField(max_length=20)
#     products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)


# short version
class CreateOrderForm(forms.ModelForm):

    class Meta:

        model = Order
        fields = ['delivery_address', 'promo_code', 'products']

