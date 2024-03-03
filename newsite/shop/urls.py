from django.urls import path
from .views import (shop_index,
                    ListProductView,
                    orders,
                    CreateProductView,
                    create_order,
                    ProductDetailsView,
                    UpdateProductView,
                    ArchivedProductView)

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
    path('products/', ListProductView.as_view(), name='products'),
    path('orders/', orders, name='orders'),
    path('product/add/', CreateProductView.as_view(), name='add_product'),
    path('order/create/', create_order, name='create_order'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='product_update'),
    path('products/<int:pk>/archived', ArchivedProductView.as_view(), name='product_archived'),
]
