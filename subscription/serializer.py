from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from profile.models import Profile
from plan.models import Plan
from plan.serializer import PlanGetSerializer
from transaction.serializer import TransactionGetSerializer

from .models import Subscription


class SubscriptionGetSerializer(BaseModelSerializer):
    transaction = TransactionGetSerializer(read_only=True)
    plan = PlanGetSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = [
            "id",
            "plan",
            "transaction",
            "start_date",
            "end_date",
            "status",
            "next_billing_date",
            "auto_renewal",
        ]


class SubscriptionCreateSerializer(BaseModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), required=True, source="profile"
    )
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.all(),
        required=True,
        source="plan",
    )

    class Meta:
        model = Subscription
        fields = [
            "id",
            "plan_id",
            "profile_id",
            "start_date",
            "end_date",
            "status",
            "next_billing_date",
            "auto_renewal",
        ]
