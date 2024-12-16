from profile.models import Contact, Profile

from django.contrib.auth import get_user_model
from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from contact.serializer import ContactSerializer

User = get_user_model()


class UserProfileSerializer(BaseModelSerializer):
    contact_info = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "contact_info", "profile_id"]

    @staticmethod
    def get_contact_info(obj):
        if obj.profile and obj.profile.contact:
            return ContactSerializer(obj.profile.contact).data
        return None

    @staticmethod
    def get_profile_id(obj):
        return obj.profile.id if obj.profile else None


class RegisterSerializer(BaseModelSerializer):
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
