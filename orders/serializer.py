from rest_framework import serializers

from orders.models import Order
from products.models import Product
from products.serializers import ProductSerializer, ProductGetSerializer
from users.models import User
from users.serializers import UserSerializer, UserListSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = [
            'user',
            'created_at',
            'updated_at',
            'total_price'
        ]

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        product = validated_data['product']
        quantity = validated_data['quantity']
        total_price = product.price * quantity

        order = Order.objects.create(
            user=user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )
        return order


class OrderListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    product = ProductGetSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "user",
            "product",
            "total_price",
        ]



