from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel


class QRMenu(BaseModel):
    branch = models.ForeignKey(
        Branch,
        related_name="employees",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    file_key = models.CharField(max_length=100)
    qr_file_key = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.branch.name} - {self.file_key}"

    class Meta:
        db_table = "qr_menu"
