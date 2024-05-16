from rest_framework import serializers
from .models import Category, Product

class CategoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_stock(self, value):
        if value == 0:
            raise serializers.ValidationError("Stock cannot be zero")
        return value

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_rating(self, value):
        min_rating = 0  
        max_rating = 10
        if value < min_rating or value > max_rating:
            raise serializers.ValidationError(f"Rating must be between {min_rating} and {max_rating}")
        return value
    
    def update(self, validated_data):
        return Product.objects.update_or_create(**validated_data)