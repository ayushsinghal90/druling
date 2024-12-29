from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from contact.models import Contact

from .models import SocialContact


class SocialContactGetSerializer(BaseModelSerializer):
    class Meta:
        model = SocialContact
        fields = [
            "id",
            "facebook",
            "x_link",
            "instagram",
            "linkedin",
            "youtube",
            "website",
        ]


class SocialContactCreateSerializer(BaseModelSerializer):
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=False,
        allow_null=True,
        source="contact",
    )

    class Meta:
        model = SocialContact
        fields = [
            "id",
            "facebook",
            "x_link",
            "instagram",
            "linkedin",
            "youtube",
            "website",
            "contact_id",
        ]
