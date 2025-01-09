from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import SubscriptionPlan


class SubscriptionPlanGetSerializer(BaseModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ["id", "amount", "name", "duration", "is_active"]


class SubscriptionPlanCreateSerializer(BaseModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ["id", "amount", "name", "duration", "is_active"]
