from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from profile.models import Profile

from ..models import Feature, ProfileFeature


class ProfileFeatureGetSerializer(BaseModelSerializer):
    class Meta:
        model = Feature
        fields = ["id", "type", "usage", "limit", "is_active"]


class ProfileFeatureCreateSerializer(BaseModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), required=True, source="profile"
    )

    class Meta:
        model = ProfileFeature
        fields = ["id", "profile_id", "type", "usage", "limit", "is_active"]
