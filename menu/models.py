from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel


class QRMenu(BaseModel):
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"menu - {self.id} {self.branch.name}"

    class Meta:
        db_table = "qr_menu"
