from django.db import models

from commons.models.BaseModel import BaseModel
from .item import Item
from .addon import Addon


class ItemAddon(BaseModel):
    item = models.ForeignKey(Item, related_name="addons", on_delete=models.CASCADE)
    addon = models.ForeignKey(Addon, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.id} - {self.addon.id}"

    class Meta:
        db_table = "item_addon"
