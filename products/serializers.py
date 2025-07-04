from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
            'is_active'
        ]



class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
            'is_active',
            'price'
        ]

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
        ]