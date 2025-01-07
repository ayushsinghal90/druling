from django.db import models

from commons.models.BaseModel import BaseModel
from resource_limit.enums import ResourceType
from subscription_plan.models import SubscriptionPlan


class ResourceLimit(BaseModel):
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    resource_type = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in ResourceType],
    )
    limit = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "resource_limit"
