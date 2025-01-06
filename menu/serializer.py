from rest_framework import serializers

from branch.models import Branch
from branch.serializer import BranchGetModelSerializer
from commons.serializer.BaseModelSerializer import BaseModelSerializer
from menu_file.serializer import MenuFileGetSerializer

from .models import QRMenu


class QRMenuGetSerializer(BaseModelSerializer):
    branch = BranchGetModelSerializer()
    files = MenuFileGetSerializer(
        many=True, fields=["id", "file_url", "order", "category"]
    )

    class Meta:
        model = QRMenu
        fields = [
            "id",
            "theme",
            "branch",
            "files",
            "is_active",
            "created_at",
            "updated_at",
        ]


class QRMenuCreateSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )

    class Meta:
        model = QRMenu
        fields = ["id", "branch_id", "theme", "is_active"]
