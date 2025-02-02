from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import BlockedEmail


class BlockedEmailSerializer(BaseModelSerializer):
    class Meta:
        model = BlockedEmail
        fields = ["id", "email", "type", "count"]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
