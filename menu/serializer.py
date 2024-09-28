from rest_framework import serializers

from branch.models import Branch

from .models import QRMenu


class QRMenuSerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )

    class Meta:
        model = QRMenu
        fields = ["id", "branch_id", "file_key"]
