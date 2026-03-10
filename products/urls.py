from django.urls import path
from .views import (
    ProductListAPIView,
    CategoryListAPIView,
    BrandListAPIView,
    CartListAPIView,
    WishlistAPIView,
    TopRatedProductsAPIView,
    PopularProductsAPIView,
    AddToCartAPIView,
    RemoveFromCartAPIView, WishlistCreateAPIView, WishlistDeleteAPIView
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('brands/', BrandListAPIView.as_view(), name='brands'),

    path('cart/', CartListAPIView.as_view(), name='cart'),
    path('cart/add/', AddToCartAPIView.as_view(), name='cart-add'),
    path('cart/remove/<int:product_id>/', RemoveFromCartAPIView.as_view(), name='cart-remove'),

    path('wishlist/', WishlistAPIView.as_view(), name='wishlist'),
    path("wishlist/add/", WishlistCreateAPIView.as_view(),name="wishlist-add"),
    path("wishlist/remove/<int:pk>/", WishlistDeleteAPIView.as_view(),name="wishlist-remove"),

    path('products/top-rated/', TopRatedProductsAPIView.as_view()),
    path('products/popular/', PopularProductsAPIView.as_view()),
]