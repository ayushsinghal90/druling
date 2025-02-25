from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel
from seat.enums import SeatStatus


class Seat(BaseModel):
    branch = models.ForeignKey(Branch, related_name="seats", on_delete=models.CASCADE)
    area = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    count = models.IntegerField(default=1)
    status = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in SeatStatus],
        db_index=True,
        default=SeatStatus.UNOCCUPIED,
    )
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.branch.name} - {self.area} - {self.name}"

    class Meta:
        db_table = "seat"
