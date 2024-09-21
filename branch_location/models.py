from django.db import models

from commons.models.BaseModel import BaseModel


class BranchLocation(BaseModel):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address}, {self.city}"

    class Meta:
        db_table = "branch_location"
