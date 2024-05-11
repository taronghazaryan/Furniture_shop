from django.db import models
from django.contrib.auth.models import User
from time import sleep
from django.core.exceptions import ValidationError

from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
def upload_product_preview(instance: 'Product', filename: str) -> str:
    return f'products/{instance.name}/preview/{filename}'


class Product(models.Model):

    name = models.CharField(max_length=20)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=True, upload_to=upload_product_preview)

    def __str__(self):

        return f'product :{self.pk}, product name: {self.name}'


def upload_product_image(instance: 'ProductImage', filename: str) -> str:
    return f'products/{instance.product.name}/images/{filename}'


def validator_image(image: 'ProductImage'):
    if not image.name.lower().endswith('jpg'):
        raise ValidationError('bad format image')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, validators=[validator_image], upload_to=upload_product_image)


class Order(models.Model):

    delivery_address = models.CharField(max_length=30)
    promo_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')


class Basket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Basket for {self.user.username} | product {self.product.name}"

