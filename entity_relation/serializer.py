from profile.models import Profile

from rest_framework import serializers

from branch.models import Branch
from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import EntityRelation


class EntityRelationSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), required=True, source="profile"
    )

    role = serializers.ChoiceField(choices=EntityRelation.ROLE_TYPE, required=True)

    class Meta:
        model = EntityRelation
        fields = ["id", "profile_id", "role", "branch_id"]
