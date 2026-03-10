from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import uuid
from orders.models import Order
from .models import Payment
from .serializers import PaymentSerializer, WebhookSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return payments that belong to the current user's orders
        return Payment.objects.filter(order__user=self.request.user)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        order_id = request.data.get("order")

        if not order_id:
            return Response(
                {"error": "Order id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if order.status == "cancelled":
            return Response(
                {"error": "Cannot pay for cancelled order"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if order.payment_status == "paid":
            return Response(
                {"error": "Order already paid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment = serializer.save(
            order=order,
            amount=order.total_price
        )

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED
        )


class PaymeWebhookAPIView(generics.GenericAPIView):

    serializer_class = WebhookSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaction_id = serializer.validated_data["transaction_id"]

        try:
            payment = Payment.objects.get(transaction_id=transaction_id)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found"},
                status=404
            )

        if payment.status == "paid":
            return Response(
                {"message": "Payment already processed"}
            )

        # Payment status update
        payment.status = "paid"
        payment.save()

        # Order payment status update
        order = payment.order
        order.payment_status = "paid"
        order.save()

        return Response({"status": "success"})

class ClickWebhookAPIView(generics.GenericAPIView):

    serializer_class = WebhookSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaction_id = serializer.validated_data["transaction_id"]

        try:
            payment = Payment.objects.get(transaction_id=transaction_id)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found"},
                status=404
            )

        if payment.status == "paid":
            return Response(
                {"message": "Payment already processed"}
            )

        # Payment status update
        payment.status = "paid"
        payment.save()

        # Order payment status update
        order = payment.order
        order.payment_status = "paid"
        order.save()

        return Response({"status": "success"})