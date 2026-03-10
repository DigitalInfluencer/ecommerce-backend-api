from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    order = serializers.IntegerField(write_only=True)

    class Meta:
        model = Payment
        fields = [
            "id",
            "order",
            "provider",
            "amount",
            "status",
            "transaction_id",
            "created_at"
        ]

        read_only_fields = [
            "amount",
            "status",
            "transaction_id",
            "created_at"
        ]

class WebhookSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()