from django.urls import path
from .views import (shop_index,
                    ListProductView,
                    CreateProductView,
                    ProductDetailsView,
                    UpdateProductView,
                    ArchivedProductView,
                    ListOrderView,
                    DetailOrderView,
                    CreateOrderView,
                    UpdateOrderView,
                    DeleteOrderView)

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
    path('products/', ListProductView.as_view(), name='products'),
    path('orders/', ListOrderView.as_view(), name='orders'),
    path('product/add/', CreateProductView.as_view(), name='add_product'),
    path('orders/create/', CreateOrderView.as_view(), name='create_order'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='product_update'),
    path('products/<int:pk>/archived', ArchivedProductView.as_view(), name='product_archived'),
    path('orders/<int:pk>/', DetailOrderView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update', UpdateOrderView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete', DeleteOrderView.as_view(), name='order_delete'),
]
