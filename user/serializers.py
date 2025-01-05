from profile.models import Contact, Profile

from django.contrib.auth import get_user_model

from commons.serializer.BaseModelSerializer import BaseModelSerializer

User = get_user_model()


class UserGetSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class RegisterSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = ("password", "email", "first_name", "last_name", "is_email_verified")
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
