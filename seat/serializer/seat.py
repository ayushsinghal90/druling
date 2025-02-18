from rest_framework import serializers

from branch.models import Branch
from commons.serializer.BaseModelSerializer import BaseModelSerializer
from seat.models import Seat


class SeatSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )

    class Meta:
        model = Seat
        fields = [
            "id",
            "branch_id",
            "area",
            "name",
            "count",
            "status",
            "note",
        ]
