from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer

from ..models import Item


class ItemAddonSerializer(BaseModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(), required=True, source="item"
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "item_id",
            "name",
            "description",
            "price",
            "ingredients",
        ]
