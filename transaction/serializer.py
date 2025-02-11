from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from profile.models import Profile
from subscription.models import Subscription

from .models import Transaction


class TransactionGetSerializer(BaseModelSerializer):
    subscription = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "discount",
            "taxes",
            "total_amount",
            "status",
            "method",
            "completed_at",
            "reference_number",
            "subscription",
        ]


class TransactionCreateSerializer(BaseModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), required=True, source="profile"
    )
    subscription_id = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all(),
        required=True,
        source="subscription",
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "profile_id",
            "subscription_id",
            "discount",
            "taxes",
            "total_amount",
            "status",
            "method",
            "completed_at",
            "reference_number",
        ]
