from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import Plan


class PlanGetSerializer(BaseModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "amount", "name", "duration", "is_active"]


class PlanCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "amount", "name", "duration", "is_active"]
