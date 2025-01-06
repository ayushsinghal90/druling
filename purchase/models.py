from django.db import models

from commons.models.BaseModel import BaseModel
from profile.models import Profile
from subscription_plan.models import SubscriptionPlan


class Purchase(BaseModel):
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_data = models.DateField(null=True, blank=True)
    end_data = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "purchase"
