from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, ProductListCreate, ProductRetrieveUpdateDestroy

app_name="shops"
urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
]
