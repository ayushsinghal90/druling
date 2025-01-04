from rest_framework import serializers


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.RegexField(
        regex=r"^\d{10}$",
        error_messages={"invalid": "Phone number must be exactly 10 digits."},
        required=False,
        allow_blank=True,
    )
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=20)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
