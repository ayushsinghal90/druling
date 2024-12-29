from rest_framework import serializers

from social_contact.requests import SocialContactSerializer


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.RegexField(
        regex=r"^\d{10}$",
        error_messages={"invalid": "Phone number must be exactly 10 digits."},
    )
    social_contact = SocialContactSerializer(required=False)
