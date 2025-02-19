from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer

from ..models import Item, Addon


class ItemAddonSerializer(BaseModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(), required=True, source="item"
    )
    addon_id = serializers.PrimaryKeyRelatedField(
        queryset=Addon.objects.all(), required=True, source="addon"
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "item_id",
            "addon_id",
        ]
