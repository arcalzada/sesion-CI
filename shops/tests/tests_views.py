import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Category, Product
from ..serializers import (
    CategoryListCreateSerializer, #TODO Implementar el resto de pruebas
    CategoryDetailSerializer,
    ProductListCreateSerializer, #TODO Implementar el resto de pruebas
    ProductDetailSerializer
)

class CategoryViewsIntegrationTests(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Electronics')
        self.category2 = Category.objects.create(name='Clothing')

    def test_list_categories(self):
        url = reverse('shops:category-list-create')
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['count'], 2)
        self.assertEqual(response_data['results'][0]['name'], self.category1.name)
        self.assertEqual(response_data['results'][1]['name'], self.category2.name)

    def test_retrieve_category(self):
        url = reverse('shops:category-detail', args=[self.category1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = CategoryDetailSerializer(self.category1)
        self.assertEqual(response.data, serializer.data)

class ProductViewsIntegrationTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product1 = Product.objects.create(
            title='Smartphone',
            description='A great smartphone',
            price=999.99,
            discount_percentage=10,
            rating=4.5,
            stock=100,
            brand='BrandName',
            category=self.category,
            thumbnail='https://example.com/thumbnail.jpg',
            images=['https://example.com/image1.jpg', 'https://example.com/image2.jpg']
        )
        self.product2 = Product.objects.create(
            title='Laptop',
            description='A powerful laptop',
            price=1499.99,
            discount_percentage=5,
            rating=4.8,
            stock=50,
            brand='BrandName',
            category=self.category,
            thumbnail='https://example.com/thumbnail.jpg',
            images=['https://example.com/image3.jpg', 'https://example.com/image4.jpg']
        )

    def test_list_products(self):
        url = reverse('shops:product-list-create')
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['count'], 2)
        self.assertEqual(response_data['results'][0]['title'], self.product1.title)
        self.assertEqual(response_data['results'][1]['title'], self.product2.title)

    def test_retrieve_product(self):
        url = reverse('shops:product-detail', args=[self.product1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ProductDetailSerializer(self.product1)
        self.assertEqual(response.data, serializer.data)