from django.shortcuts import render

from rest_framework import generics
from .models import Order, OrderItem
from delivery.models import Address
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import CartItem
from .serializers import OrderSerializer, CheckoutSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .tasks import send_order_email,send_order_cancel_email
class OrderListAPIView(generics.ListAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ["status"]

    search_fields = [
        "id",
    ]

    ordering_fields = [
        "created_at",
        "total_price"
    ]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

from django.db import transaction

class CheckoutAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=CheckoutSerializer,
        responses={201: None}
    )
    @transaction.atomic
    def post(self, request):

        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        address = serializer.validated_data["address"]

        cart_items = CartItem.objects.filter(user=user).select_related("product")

        if not cart_items.exists():
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        total_price = 0

        order = Order.objects.create(
            user=user,
            address=address,
            total_price=0
        )

        for item in cart_items:

            product = item.product

            if product.stock < item.quantity:
                return Response(
                    {"error": f"{product.name} not enough stock"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                price=item.price
            )

            product.stock -= item.quantity
            product.save(update_fields=["stock"])

            total_price += item.price * item.quantity

        order.total_price = total_price
        order.save(update_fields=["total_price"])

        transaction.on_commit(
            lambda: send_order_email.delay(
                user.email,
                order.id
            )
        )

        cart_items.delete()

        return Response(
            {
                "message": "Order created successfully",
                "order_id": order.id,
                "total_price": total_price
            },
            status=status.HTTP_201_CREATED
        )


class CancelOrderAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def patch(self, request, pk):

        order = get_object_or_404(Order, id=pk, user=request.user)

        if order.status != "pending":
            return Response(
                {"error": "Only pending orders can be cancelled"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for item in order.items.select_related("product"):

            product = item.product
            product.stock += item.quantity
            product.save(update_fields=["stock"])

        order.status = "cancelled"
        order.save(update_fields=["status"])

        # cancel email
        transaction.on_commit(
            lambda: send_order_cancel_email.delay(
                order.user.email,
                order.id
            )
        )

        return Response(
            {"message": "Order cancelled successfully"},
            status=status.HTTP_200_OK
        )