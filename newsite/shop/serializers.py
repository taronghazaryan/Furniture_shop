from rest_framework import serializers

from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = [
            "pk",
            "name",
            "description",
            "price",
            "created_at",
            "archived",
        ]


class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = [
            "pk",
            "delivery_address",
            "promo_code",
            "created_at",
            "user",
            "products",
        ]
