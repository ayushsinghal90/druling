from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel
from item.models import Item


class Favourite(BaseModel):
    branch = models.ForeignKey(
        Branch, related_name="favourites", on_delete=models.CASCADE
    )
    item = models.ForeignKey(Item, related_name="favourites", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} - {self.branch.name}"

    class Meta:
        db_table = "favourite"
