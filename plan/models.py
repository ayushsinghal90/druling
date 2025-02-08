from django.db import models

from commons.models.BaseModel import BaseModel
from plan.enum import Product, PlanType


class Plan(BaseModel):
    amount = models.IntegerField()
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    is_active = models.BooleanField(default=True)
    product = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in Product],
        db_index=True,
    )
    plan_type = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in PlanType],
        db_index=True,
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "plan"
        indexes = [
            models.Index(
                fields=["product", "plan_type"], name="plan_product_plan_type_idx"
            ),
        ]
