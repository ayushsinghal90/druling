import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from .addon import AddonService
from ..models import ItemAddon
from ..serializer import ItemAddonSerializer

logger = logging.getLogger(__name__)


class ItemAddonService(BaseService):
    def __init__(self, addon_service=None):
        super().__init__(ItemAddon)
        self.addon_service = addon_service or AddonService()

    def create(self, item_id, data):
        with transaction.atomic():
            addon_data = data.pop("addons")
            addon = self.addon_service.create(addon_data)

            item_addon = ItemAddonSerializer(
                data={"addon_id": addon.id, "item_id": item_id}
            )
            if item_addon.is_valid(raise_exception=True):
                item_addon.save(item_id=item_id)
                return item_addon
