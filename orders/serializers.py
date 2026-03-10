from rest_framework import serializers
from .models import Order, OrderItem
from delivery.models import Address

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "address",
            "total_price",
            "status",
            "payment_status",
            "created_at",
            "items"
        ]

        read_only_fields = [
            "total_price",
            "status",
            "payment_status",
            "created_at"
        ]

class CheckoutSerializer(serializers.Serializer):
    address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all()
    )