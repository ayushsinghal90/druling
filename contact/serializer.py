from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import Contact


class ContactSerializer(BaseModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "email", "phone_number"]
