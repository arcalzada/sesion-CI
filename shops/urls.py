from django.urls import path
from .views import CategoryList, CategoryRetrieve, ProductList, ProductRetrieve

app_name="shops"
urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieve.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieve.as_view(), name='product-detail'),
]
