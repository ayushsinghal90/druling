from django.db import models

from commons.models.BaseModel import BaseModel
from ..enums import FeatureType
from plan.models import Plan


class Feature(BaseModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in FeatureType],
        db_index=True,
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    limit = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.type}"

    class Meta:
        db_table = "feature"
