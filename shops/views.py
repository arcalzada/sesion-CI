from rest_framework import generics, status
from .models import Category, Product
from .serializers import CategoryListSerializer, CategoryDetailSerializer, ProductListSerializer, ProductDetailSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        rating = self.request.query_params.get('rating')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        category_id = self.request.query_params.get('category_id')

        # Validar que solo los parámetros especificados estén presentes
        allowed_params = {'title', 'rating', 'min_price', 'max_price', 'category_id', 'page'} #OJO: Incluir page
        request_params = set(self.request.query_params.keys())
        invalid_params = request_params - allowed_params
        if invalid_params:
            raise ValidationError(f'Parámetros no válidos: {invalid_params}')
        
        # Manejo de errores para valores de parámetros no válidos
        try:
            if rating is not None:
                rating = float(rating)
            if min_price is not None:
                min_price = float(min_price)
            if max_price is not None:
                max_price = float(max_price)
            if category_id is not None:
                category_id = int(category_id)
        except (ValueError, TypeError) as e:
            raise ValidationError("Los parámetros de consulta deben ser del tipo correcto.")

        # Filtrar queryset según los parámetros de consulta
        if title:
            queryset = queryset.filter(title__icontains=title)
        if rating:
            queryset = queryset.filter(rating=rating)
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            invalid_params = exc.detail
            return Response({'error': f'Parámetros no válidos: {invalid_params}'}, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)
    
class ProductRetrieve(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer