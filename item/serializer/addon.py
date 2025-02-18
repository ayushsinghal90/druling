from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer

from ..models import Item


class AddonSerializer(BaseModelSerializer):
    ingredients = serializers.JSONField()

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "price",
            "remaining_quantities",
            "ingredients",
        ]
