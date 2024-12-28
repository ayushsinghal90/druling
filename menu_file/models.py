from django.db import models

from commons.models.BaseModel import BaseModel
from menu.models import QRMenu


class MenuFile(BaseModel):
    menu = models.ForeignKey(
        QRMenu,
        related_name="files",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    file_key = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.file_key}"

    class Meta:
        db_table = "menu_file"
