from django.urls import path
from .views import shop_index, products, orders, add_product, create_order, ProductDetails

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
    path('products/', products, name='products'),
    path('orders/', orders, name='orders'),
    path('add_product/', add_product, name='add_product'),
    path('create_order/', create_order, name='create_order'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='details'),
]
