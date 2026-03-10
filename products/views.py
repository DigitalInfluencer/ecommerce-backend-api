from rest_framework import generics, filters, serializers
from .models import Product, Category, Brand, CartItem, Wishlist
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    BrandSerializer,
    CartItemSerializer,
    WishlistSerializer,
    RemoveFromCartSerializer
)
from django.db.models import Q
from django.core.cache import cache
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
class ProductListAPIView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):

        queryset = Product.objects.filter(is_active=True)

        # 🔎 Search
        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )

        # 🎛 Category filter
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)

        # 💰 Price filter
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        # 📊 Ordering
        ordering = self.request.query_params.get("ordering")

        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset


    def list(self, request, *args, **kwargs):

        cache_key = f"product_list_{request.get_full_path()}"

        cached_products = cache.get(cache_key)

        if cached_products:
            return Response(cached_products)

        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        cache.set(cache_key, serializer.data, timeout=60 * 5)

        return Response(serializer.data)


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):

        cached_categories = cache.get("categories")

        if cached_categories:
            return Response(cached_categories)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        cache.set("categories", serializer.data, timeout=60 * 10)

        return Response(serializer.data)


class BrandListAPIView(generics.ListAPIView):

    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):

        cached_brands = cache.get("brands")

        if cached_brands:
            return Response(cached_brands)

        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)

        cache.set("brands", serializer.data, timeout=60 * 10)

        return Response(serializer.data)


class CartListAPIView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

class AddToCartAPIView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={
                "quantity": quantity,
                "price": product.price
            }
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RemoveFromCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):

        try:
            cart_item = CartItem.objects.get(
                user=request.user,
                product_id=product_id
            )

            cart_item.delete()

            return Response(
                {"message": "Item removed from cart"},
                status=status.HTTP_200_OK
            )

        except CartItem.DoesNotExist:
            return Response(
                {"error": "Item not found in cart"},
                status=status.HTTP_404_NOT_FOUND
            )

class WishlistAPIView(generics.ListAPIView):

    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

class WishlistCreateAPIView(generics.CreateAPIView):

    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        product = serializer.validated_data["product"]

        if Wishlist.objects.filter(
            user=self.request.user,
            product=product
        ).exists():

            raise serializers.ValidationError(
                {"error": "Product already in wishlist"}
            )

        serializer.save(user=self.request.user)
class WishlistDeleteAPIView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get("pk")

        try:
            wishlist_item = Wishlist.objects.get(
                id=pk,
                user=request.user
            )
        except Wishlist.DoesNotExist:
            return Response(
                {"error": "Product not found in wishlist"},
                status=status.HTTP_404_NOT_FOUND
            )

        wishlist_item.delete()

        return Response(
            {"message": "Product removed from wishlist"},
            status=status.HTTP_200_OK
        )

class TopRatedProductsAPIView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get(self, request):

        cached_products = cache.get("top_rated_products")

        if cached_products:
            return Response(cached_products)

        products = Product.objects.filter(is_active=True).order_by('-rating')[:10]
        serializer = ProductSerializer(products, many=True)

        cache.set("top_rated_products", serializer.data, timeout=60 * 5)

        return Response(serializer.data)

class PopularProductsAPIView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get(self, request):

        cached_products = cache.get("popular_products")

        if cached_products:
            return Response(cached_products)

        products = Product.objects.filter(is_active=True).order_by('-review_count')[:10]
        serializer = ProductSerializer(products, many=True)

        cache.set("popular_products", serializer.data, timeout=60 * 5)

        return Response(serializer.data)