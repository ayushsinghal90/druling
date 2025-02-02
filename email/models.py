from django.db import models

from commons.models.BaseModel import BaseModel
from email.enums.blocked_type import BlockedType


class BlockedEmail(BaseModel):
    email = models.EmailField(blank=True, null=True, db_index=True, unique=True)
    type = models.CharField(
        max_length=50,
        choices=BlockedType.choices(),
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id} - {self.type}"

    class Meta:
        db_table = "blocked_email"
