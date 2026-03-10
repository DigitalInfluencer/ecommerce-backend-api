from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Address
        fields = "__all__"
        read_only_fields = ['user']