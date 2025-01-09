from django.db import models

from commons.models.BaseModel import BaseModel
from profile.models import Profile
from subscription.models import Subscription
from transaction.enums import TransactionStatus


class Transaction(BaseModel):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.IntegerField()
    discount = models.IntegerField(default=0)
    taxes = models.IntegerField(default=0)
    total_amount = models.IntegerField()
    status = models.CharField(
        max_length=50,
        choices=TransactionStatus.choices(),
        default=TransactionStatus.PENDING,
    )
    method = models.CharField(max_length=50, null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    reference_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id}, {self.subscription.id}"

    class Meta:
        db_table = "transaction"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["profile", "-created_at"]),
            models.Index(fields=["status", "-created_at"]),
        ]
