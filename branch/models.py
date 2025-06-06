from django.db import models

from branch_location.models import BranchLocation
from commons.models.BaseModel import BaseModel
from contact.models import Contact
from restaurant.models import Restaurant


class Branch(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant, related_name="branches", on_delete=models.CASCADE
    )
    location = models.OneToOneField(BranchLocation, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    contact = models.ForeignKey(
        Contact,
        related_name="branches",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.location.city}"

    class Meta:
        db_table = "branch"
