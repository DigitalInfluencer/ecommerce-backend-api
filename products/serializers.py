from rest_framework import serializers
from .models import Category, Brand, Product, CartItem, Wishlist


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "name",
            "slug",
            "description",
            "image",
            "parent",
            "created_at"
        ]

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source="category.name", read_only=True)
    brand = serializers.CharField(source="brand.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "description",
            "price",
            "discount_price",
            "stock",
            "category",
            "brand",
            "image",
            "rating",
            "review_count",
            "created_at"
        ]


class CartItemSerializer(serializers.ModelSerializer):

    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = [
            "product",
            "quantity",
            "price",
            "total_price",
            "created_at"
        ]

        read_only_fields = [
            "price",
            "total_price",
            "created_at"
        ]


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = [
            "product",
            "created_at"
        ]

        read_only_fields = ["created_at"]

class RemoveFromCartSerializer(serializers.Serializer):
    product = serializers.IntegerField()