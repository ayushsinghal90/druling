from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import BranchLocation


class BranchLocationSerializer(BaseModelSerializer):
    class Meta:
        model = BranchLocation
        fields = ["id", "address", "city", "state", "postal_code", "country"]
