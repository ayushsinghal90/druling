import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import SeatOrder
from ..serializer import SeatOrderSerializer

logger = logging.getLogger(__name__)


class SeatOrderService(BaseService):
    def __init__(self):
        super().__init__(SeatOrder)

    def create(self, order, seat_id):
        with transaction.atomic():
            serializer = SeatOrderSerializer(
                data={"seat_id": seat_id, "order_id": order.id}
            )
            serializer.is_valid(raise_exception=True)
            return serializer.save()

    def get_all(self, branch):
        try:
            return SeatOrder.objects.filter(branch=branch)
        except Exception as e:
            logger.error(f"Error fetching features: {e}")
            return []
