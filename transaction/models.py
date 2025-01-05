from django.db import models

from commons.models.BaseModel import BaseModel
from profile.models import Profile


class Transaction(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.id}, {self.profile.id}"

    class Meta:
        db_table = "transaction"
