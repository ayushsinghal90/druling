from rest_framework import serializers

from subscription_plan.models import SubscriptionPlan


class TransactionSerializer(serializers.Serializer):
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=SubscriptionPlan.objects.all(), required=True
    )
