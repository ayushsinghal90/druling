from django.db import models

from commons.models.BaseModel import BaseModel


class Addon(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_quantities = models.PositiveIntegerField(default=0)
    ingredients = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = "addon"
