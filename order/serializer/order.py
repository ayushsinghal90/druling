from rest_framework import serializers

from branch.models import Branch
from commons.serializer.BaseModelSerializer import BaseModelSerializer

from ..models import Order


class OrderSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "branch_id",
            "note",
            "status",
        ]
