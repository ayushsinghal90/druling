from django.db import models

from commons.models.BaseModel import BaseModel
from contact.models import Contact


class Restaurant(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        related_name="restaurant",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "restaurant"
