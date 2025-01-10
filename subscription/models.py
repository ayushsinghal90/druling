from django.db import models

from commons.models.BaseModel import BaseModel
from profile.models import Profile
from subscription.enums import SubscriptionStatus
from subscription_plan.models import SubscriptionPlan


class Subscription(BaseModel):
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    cancellation_date = models.DateField(null=True, blank=True)
    next_billing_date = models.DateField(null=True, blank=True)
    auto_renewal = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50,
        choices=SubscriptionStatus.choices(),
        default=SubscriptionStatus.DRAFT,
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "subscription"
