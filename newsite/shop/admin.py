from django.contrib import admin
from .models import Product, Order
from django.db.models import QuerySet
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)