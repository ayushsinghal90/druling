from rest_framework import serializers

from branch.models import Branch

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
    ingredients = serializers.JSONField()

    class Meta:
        model = Item
        fields = [
            "id",
            "branch_id",
            "name",
            "description",
            "price",
            "remaining_quantities",
            "ingredients",
        ]

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
