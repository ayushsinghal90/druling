import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from .item_addon import ItemAddonService
from .item_variation import ItemVariationService
from ..models import Item
from ..serializer import ItemSerializer

logger = logging.getLogger(__name__)


class ItemService(BaseService):
    def __init__(self, item_addon_service=None, item_variation_service=None):
        super().__init__(Item)
        self.item_addon_service = item_addon_service or ItemAddonService()
        self.item_variation_service = item_variation_service or ItemVariationService()

    def create(self, data):
        with transaction.atomic():
            branch_id = data.pop("branch_id")

            item_serializer = ItemSerializer(data=data)
            if item_serializer.is_valid(raise_exception=True):
                item = item_serializer.save(branch_id=branch_id)

                self.item_addon_service.bulk_create(item.id, data.get("addons"))
                self.item_variation_service.bulk_create(item.id, data.get("variations"))

                return item
