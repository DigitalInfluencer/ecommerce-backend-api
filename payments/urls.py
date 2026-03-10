from django.urls import path
from .views import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymeWebhookAPIView,
    ClickWebhookAPIView
)

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
    path('payments/create/', PaymentCreateAPIView.as_view(), name='create-payment'),

    path('payments/webhook/payme/', PaymeWebhookAPIView.as_view(), name='payme-webhook'),
    path('payments/webhook/click/', ClickWebhookAPIView.as_view(), name='click-webhook'),
]