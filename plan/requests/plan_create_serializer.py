from rest_framework import serializers

from feature.requests import FeatureSerializer
from plan.requests.serlializers import PlanSerializer


class PlanCreateSerializer(serializers.Serializer):
    plan = PlanSerializer()
    features = serializers.ListField(child=FeatureSerializer())
