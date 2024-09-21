from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    ingredients = serializers.JSONField()

    class Meta:
        model = Item
        fields = [
            "id",
            "branch",
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
