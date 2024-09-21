from rest_framework import serializers

from contact.models import Contact
from contact.serializer import ContactSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    contact = ContactSerializer()
    branch = serializers.StringRelatedField()
    role = serializers.ChoiceField(choices=Profile.PROFILE_TYPE)

    class Meta:
        model = Profile
        fields = ["id", "user", "role", "branch", "contact"]

    def create(self, validated_data):
        contact_data = validated_data.pop("contact")
        contact = Contact.objects.create(**contact_data)
        profile = Profile.objects.create(contact=contact, **validated_data)
        return profile

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact", None)

        if contact_data:
            Contact.objects.filter(id=instance.contact.id).update(**contact_data)

        return super().update(instance, validated_data)
