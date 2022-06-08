from rest_framework import serializers
from .models import (
    Product,
    ProductCategory,
    Brand
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description']
        read_only_fields = ['created_at']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']
        read_only_fields = ['created_at']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["name",]
        read_only_fields = ["created_at",]