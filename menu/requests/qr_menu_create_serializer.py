from rest_framework import serializers

from branch.models import Branch
from menu_file.requests import MenuFileSerializer


class CreateQRMenuSerializer(serializers.Serializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
    theme = serializers.CharField(max_length=100, required=False, default="default")
    files = MenuFileSerializer(many=True, required=True)
