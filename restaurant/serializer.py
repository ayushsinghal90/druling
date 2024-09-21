from rest_framework import serializers

from contact.models import Contact
from contact.serializer import ContactSerializer

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "contact"]

    def create(self, validated_data):
        contact_data = validated_data.pop("contact")
        contact = Contact.objects.create(**contact_data)
        restaurant = Restaurant.objects.create(contact=contact, **validated_data)
        return restaurant

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact", None)
        if contact_data:
            Contact.objects.filter(id=instance.contact.id).update(**contact_data)
        return super().update(instance, validated_data)
