from django.test import SimpleTestCase, TestCase
from ..models import Product, Category

#Test unitarios (SimpleTestCase)
class CategoryModelSimpleTestCase(SimpleTestCase):
    def test_str_representation(self):
        category = Category(name="Electronics")
        self.assertEqual(str(category), "Electronics")

class ProductModelSimpleTestCase(SimpleTestCase):
    def test_str_representation(self):
        product = Product(title="Smartphone")
        self.assertEqual(str(product), "Smartphone")

#Test integraciones (TestCase)
class CategoryModelTestCase(TestCase):
    def test_unique_name_constraint(self):
        Category.objects.create(name="Electronics")
        with self.assertRaises(Exception):
            Category.objects.create(name="Electronics") 

class ProductModelTestCase(TestCase):
    def test_product_unique_title(self):
        category = Category.objects.create(name="Electronics")
        Product.objects.create(
            title="Smartphone",
            description="A great smartphone",
            price=999.99,
            discount_percentage=10,
            rating=4.5,
            stock=100,
            brand="BrandX",
            category=category,
            thumbnail="https://example.com/thumbnail.jpg",
            images=["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
        )
        with self.assertRaises(Exception):
            Product.objects.create(
                title="Smartphone",  # Título duplicado
                description="Another smartphone",
                price=799.99,
                discount_percentage=5,
                rating=4.0,
                stock=50,
                brand="BrandY",
                category=self.product.category,
                thumbnail="https://example.com/another-thumbnail.jpg",
                images=["https://example.com/image3.jpg"]
            )