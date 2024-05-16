from django.test import TestCase
from ..models import Category, Product
from ..serializers import (
    CategoryListCreateSerializer,
    CategoryDetailSerializer,
    ProductListCreateSerializer,
    ProductDetailSerializer
)

class CategorySerializerTests(TestCase):
    def test_category_list_create_serializer_valid(self):
        serializer = CategoryListCreateSerializer(data={'name': 'Electronics'})
        self.assertTrue(serializer.is_valid())

    def test_category_detail_serializer_valid(self):
        category = Category.objects.create(name='Electronics')
        serializer = CategoryDetailSerializer(category)
        self.assertTrue(serializer.data['id'] == category.id)

class ProductSerializerTests(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Category 1')
        self.data = {
            'title': 'Smartphone',
            'description': 'A great smartphone',
            'price': '999.99', 
            'discount_percentage': '0.00', 
            'rating': '4.5', 
            'stock': 100,
            'brand': 'BrandName',
            'category': 1,  
            'thumbnail': 'https://example.com/thumbnail.jpg',
            'images': []  #
        }

    def test_product_list_create_serializer_valid(self):
        serializer = ProductListCreateSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_product_list_create_serializer_invalid_stock_zero(self):
        serializer = ProductListCreateSerializer(data={'title': 'Smartphone', 'price': 999.99, 'stock': 0})
        self.assertFalse(serializer.is_valid())
        self.assertIn('stock', serializer.errors)

    def test_product_detail_serializer_valid(self):
        serializer = ProductDetailSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_product_detail_serializer_invalid_rating_out_of_range(self):
        serializer = ProductDetailSerializer(data={'title': 'Smartphone', 'price': 999.99, 'stock': 100, 'rating': 100})
        self.assertFalse(serializer.is_valid())
        self.assertIn('rating', serializer.errors)
