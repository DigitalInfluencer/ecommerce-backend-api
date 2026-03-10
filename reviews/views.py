from django.shortcuts import render

from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from orders.models import OrderItem
from .models import Review
from .serializers import ReviewSerializer


class ReviewCreateAPIView(generics.CreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        product = serializer.validated_data["product"]

        purchased = OrderItem.objects.filter(
            order__user=self.request.user,
            product=product,
            order__status="delivered"
        ).exists()

        if not purchased:
            raise serializers.ValidationError(
                {"error": "You can review only purchased products"}
            )
        if Review.objects.filter(
            user=self.request.user,
            product=product
        ).exists():

            raise serializers.ValidationError(
                {"error": "You already reviewed this product"}
            )

        serializer.save(user=self.request.user)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)