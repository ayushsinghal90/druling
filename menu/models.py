from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel


class QRMenu(BaseModel):
    branch = models.OneToOneField(
        Branch,
        related_name="qr_menu",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    theme = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"menu - {self.id} {self.branch.name}"

    class Meta:
        db_table = "qr_menu"
