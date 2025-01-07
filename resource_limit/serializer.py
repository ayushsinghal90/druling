from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import ResourceLimit


class ResourceLimitSerializer(BaseModelSerializer):
    class Meta:
        model = ResourceLimit
        fields = ["id", "amount", "profile"]
