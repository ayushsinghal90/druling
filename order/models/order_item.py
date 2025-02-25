from django.db import models

from commons.models.BaseModel import BaseModel
from item.models import Item, ItemVariation, ItemAddon
from order.enums import ItemStatus
from order.models.order import Order


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    variation = models.ForeignKey(
        ItemVariation, on_delete=models.SET_NULL, null=True, blank=True
    )
    addons = models.ForeignKey(
        Item, related_name="order_item", on_delete=models.CASCADE
    )
    note = models.CharField(max_length=200, blank=True, null=True)
    addon = models.ManyToManyField(ItemAddon, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in ItemStatus],
        db_index=True,
        default=ItemStatus.PENDING,
    )

    def __str__(self):
        return f"{self.id} - {self.order.id}"

    class Meta:
        db_table = "order_item"
