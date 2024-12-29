from commons.serializer.BaseModelSerializer import BaseModelSerializer
from social_contact.serializer import SocialContactGetSerializer

from .models import Contact


class ContactSerializer(BaseModelSerializer):
    social_contact = SocialContactGetSerializer(source="socials", required=False)

    class Meta:
        model = Contact
        fields = ["id", "email", "phone_number", "social_contact"]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Remove `social_contact` if it is None or empty
        if not representation.get("social_contact") or not representation[
            "social_contact"
        ].get("id"):
            representation.pop("social_contact", None)

        return representation
