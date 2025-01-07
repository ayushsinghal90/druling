from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import Subscription


class SubscriptionSerializer(BaseModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "amount", "profile"]
