from rest_framework import serializers

from branch_location.models import BranchLocation
from branch_location.serializer import BranchLocationSerializer
from contact.models import Contact
from contact.serializer import ContactSerializer

from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    location = BranchLocationSerializer()
    contact = ContactSerializer()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Branch
        fields = ["id", "name", "location", "contact", "restaurant"]

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        contact_data = validated_data.pop("contact")
        location = BranchLocation.objects.create(**location_data)
        contact = Contact.objects.create(**contact_data)
        branch = Branch.objects.create(
            location=location, contact=contact, **validated_data
        )
        return branch

    def update(self, instance, validated_data):
        location_data = validated_data.pop("location", None)
        contact_data = validated_data.pop("contact", None)

        if location_data:
            BranchLocation.objects.filter(id=instance.location.id).update(
                **location_data
            )

        if contact_data:
            Contact.objects.filter(id=instance.contact.id).update(**contact_data)

        return super().update(instance, validated_data)
