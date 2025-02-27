from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel
from order.enums.status import OrderStatus


class Order(BaseModel):
    branch = models.ForeignKey(Branch, related_name="orders", on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in OrderStatus],
        db_index=True,
        default=OrderStatus.PENDING,
    )

    def __str__(self):
        return f"{self.item.name} - {self.branch.name}"

    class Meta:
        db_table = "order"
