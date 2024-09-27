from rest_framework import serializers

from contact.serializer import ContactSerializer

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "contact"]

    def create(self, validated_data):
        return super().create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
