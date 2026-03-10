from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings

from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterSerializer, GoogleLoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class GoogleLoginView(APIView):

    @extend_schema(request=GoogleLoginSerializer)
    def post(self, request):

        token = request.data.get("token")

        if not token:
            return Response({"error": "Token is required"}, status=400)

        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )

            email = idinfo.get("email")
            first_name = idinfo.get("given_name", "")
            last_name = idinfo.get("family_name", "")

            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "username": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "provider": "google"
                }
            )

            refresh = RefreshToken.for_user(user)

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })

        except ValueError:
            return Response({"error": "Invalid Google token"}, status=400)