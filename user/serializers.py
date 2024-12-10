from profile.models import Contact, Profile

from django.contrib.auth import get_user_model
from rest_framework import serializers

from contact.serializer import ContactSerializer

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    contact_info = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "contact_info"]

    @staticmethod
    def get_contact_info(obj):
        if obj.profile and obj.profile.contact:
            return ContactSerializer(obj.profile.contact).data
        return None


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "password",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {field: {"required": True} for field in fields}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        contact_instance = Contact.objects.create(email=validated_data.get("email"))
        Profile.objects.create(user=user, contact=contact_instance)
        return user
