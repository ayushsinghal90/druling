from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel
from item.models import Item


class Order(BaseModel):
    branch = models.ForeignKey(
        Branch, related_name="customer_favourites", on_delete=models.CASCADE
    )
    item = models.ForeignKey(Item, related_name="favourites", on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.item.name} - {self.branch.name}"

    class Meta:
        db_table = "order"
