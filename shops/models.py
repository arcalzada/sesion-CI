from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta: 
        ordering=('id',) 

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    thumbnail = models.URLField()
    images = models.JSONField()

    class Meta: 
        ordering=('id',) 

    def __str__(self):
        return self.title
