from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from plan.models import Plan

from ..models import Feature


class FeatureGetSerializer(BaseModelSerializer):
    class Meta:
        model = Feature
        fields = ["id", "type", "description", "limit", "is_active"]


class FeatureCreateSerializer(BaseModelSerializer):
    plan = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.all(),
        required=True,
        source="plan",
    )

    class Meta:
        model = Feature
        fields = ["id", "plan", "type", "description", "limit", "is_active"]
