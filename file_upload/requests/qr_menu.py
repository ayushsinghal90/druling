from rest_framework import serializers

from branch.models import Branch


class QRMenuUploadSerializer(serializers.Serializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
