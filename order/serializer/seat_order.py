from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from seat.models import Seat

from ..models import SeatOrder, Order


class SeatOrderSerializer(BaseModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), required=True, source="order"
    )
    seat_id = serializers.PrimaryKeyRelatedField(
        queryset=Seat.objects.all(), required=True, source="item"
    )

    class Meta:
        model = SeatOrder
        fields = [
            "id",
            "order_id",
            "seat_id",
        ]
