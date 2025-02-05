from rest_framework import serializers

from plan.models import Plan


class TransactionSerializer(serializers.Serializer):
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.all(), required=True
    )
