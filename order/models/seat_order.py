from django.db import models

from commons.models.BaseModel import BaseModel
from order.models.order import Order
from seat.models import Seat


class SeatOrder(BaseModel):
    seat = models.ForeignKey(Seat, related_name="orders", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="seats", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.seat.id} - {self.order.id}"

    class Meta:
        db_table = "seat_order"
