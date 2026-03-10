from django.urls import path
from .views import AddressListCreateAPIView, AddressDetailAPIView

urlpatterns = [
    path('address/', AddressListCreateAPIView.as_view(), name='address-list'),
    path('address/<int:pk>/', AddressDetailAPIView.as_view(), name='address-detail'),
]