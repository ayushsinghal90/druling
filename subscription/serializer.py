from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from profile.models import Profile
from subscription_plan.models import SubscriptionPlan

from .models import Subscription


class SubscriptionGetSerializer(BaseModelSerializer):
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
        queryset=SubscriptionPlan.objects.all(),
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
