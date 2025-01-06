from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import SubscriptionPlan


class PurchaseSerializer(BaseModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ["id", "amount", "profile"]
