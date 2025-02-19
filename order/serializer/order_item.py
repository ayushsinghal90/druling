from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from item.models import Item, ItemVariation

from ..models import OrderItem, Order


class OrderItemSerializer(BaseModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), required=True, source="order"
    )
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(), required=True, source="item"
    )
    variation_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemVariation.objects.all(), required=False, source="variation"
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order_id",
            "item_id",
            "variation_id",
            "addons",
            "note",
            "quantity",
            "price",
        ]
