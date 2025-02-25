from rest_framework import serializers

from branch.models import Branch
from commons.serializer.BaseModelSerializer import BaseModelSerializer
from item.models import Item

from ..models import CustomerFavourite


class CustomerFavouriteSerializer(BaseModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(), required=True, source="item"
    )

    class Meta:
        model = CustomerFavourite
        fields = [
            "id",
            "branch_id",
            "item_id",
            "note",
        ]
