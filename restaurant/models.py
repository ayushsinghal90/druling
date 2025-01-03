from django.db import models

from commons.models.BaseModel import BaseModel
from contact.models import Contact


class Restaurant(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    img_url = models.CharField(max_length=200, null=True, blank=True)
    contact = models.ForeignKey(
        Contact,
        related_name="restaurant",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "restaurant"
