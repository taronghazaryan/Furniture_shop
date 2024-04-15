from django.urls import path, include
from .views import (shop_index,
                    ListProductView,
                    CreateProductView,
                    ProductDetailsView,
                    UpdateProductView,
                    ArchivedProductView,
                    # ListOrderView,
                    DetailOrderView,
                    CreateOrderView,
                    UpdateOrderView,
                    DeleteOrderView,
                    user_orders,
                    OrderViewSet,
                    ProductViewSet,
                    add_basket,
                    delete_basket)

from rest_framework.routers import DefaultRouter

app_name = 'shop'

routers = DefaultRouter()
routers.register("products", ProductViewSet)
routers.register("orders", OrderViewSet)

urlpatterns = [
    path('', shop_index, name='index'),
    path('api/', include(routers.urls)),
    path('products/', ListProductView.as_view(), name='products'),
    # path('orders/', ListOrderView.as_view(), name='orders'),
    path('product/add/', CreateProductView.as_view(), name='add_product'),
    path('orders/create/', CreateOrderView.as_view(), name='create_order'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='product_update'),
    path('products/<int:pk>/archived', ArchivedProductView.as_view(), name='product_archived'),
    path('orders/<int:pk>/', DetailOrderView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update', UpdateOrderView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete', DeleteOrderView.as_view(), name='order_delete'),
    path('orders/', user_orders, name='orders'),
    path('add_basket/<int:product_pk>/', add_basket, name='add_basket'),
    path('delete_basket/<int:product_id>/', delete_basket, name='delete_basket'),
]
