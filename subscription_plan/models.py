from django.db import models

from commons.models.BaseModel import BaseModel


class SubscriptionPlan(BaseModel):
    amount = models.IntegerField()
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "subscription_plan"
