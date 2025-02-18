import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import Item
from ..serializer import ItemSerializer

logger = logging.getLogger(__name__)


class ItemService(BaseService):
    def __init__(self):
        super().__init__(Item)

    def create(self, data):
        with transaction.atomic():
            branch_id = data.pop("branch_id")

            item = ItemSerializer(data=data)
            if item.is_valid(raise_exception=True):
                item.save(branch_id=branch_id)
                return item.data
