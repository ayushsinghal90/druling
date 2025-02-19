import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import Seat
from ..serializer import SeatSerializer

logger = logging.getLogger(__name__)


class SeatService(BaseService):
    def __init__(self):
        super().__init__(Seat)

    def create(self, data):
        with transaction.atomic():
            branch_id = data.pop("branch_id")

            seat_serializer = SeatSerializer(data=data)
            seat_serializer.is_valid(raise_exception=True)
            return seat_serializer.save(branch_id=branch_id)
