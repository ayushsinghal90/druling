from django.db import models

from commons.models.BaseModel import BaseModel
from item.models import Item


class ItemVariation(BaseModel):
    item = models.ForeignKey(Item, related_name="variations", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = "item_variation"
