from django.urls import path
from .views import RegisterView
from .views import GoogleLoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("auth/google/", GoogleLoginView.as_view()),
]