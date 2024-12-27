from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.RegexField(
        regex=r"^\d{10}$",
        error_messages={"invalid": "Phone number must be exactly 10 digits."},
    )
