from rest_framework import serializers

from branch.models import Branch
from menu_file.requests import MenuFileSerializer


class CreateQRMenuSerializer(serializers.Serializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
    files = MenuFileSerializer(many=True, required=True)
