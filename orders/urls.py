from django.urls import path
from .views import OrderListAPIView, CheckoutAPIView, OrderDetailAPIView, CancelOrderAPIView

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name='orders'),
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
    path(
    "orders/<int:pk>/cancel/", CancelOrderAPIView.as_view(), name="order-cancel"),
]