from rest_framework import serializers

from branch.models import Branch
from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import QRMenu


class QRMenuSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )

    class Meta:
        model = QRMenu
        fields = ["id", "branch_id", "file_key"]


class UploadMenuSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )

    class Meta:
        model = QRMenu
        fields = ["branch_id", "file_key"]
        extra_kwargs = {field: {"required": True} for field in fields}
