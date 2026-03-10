from django.urls import path
from .views import ReviewCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path('reviews/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]