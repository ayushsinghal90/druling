from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from feature.serializer import FeatureGetSerializer

from .models import Plan


class PlanGetSerializer(BaseModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ["id", "amount", "name", "duration", "is_active", "features"]

    @staticmethod
    def get_features(obj):
        if obj.feature_set:
            return FeatureGetSerializer(obj.feature_set, many=True).data
        return None


class PlanCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "amount", "name", "duration", "is_active"]
