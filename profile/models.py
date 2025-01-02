from django.db import models

from commons.models.BaseModel import BaseModel
from contact.models import Contact
from user.models import User


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    img_url = models.CharField(max_length=200, null=True, blank=True)
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE, related_name="contact", null=True, blank=True
    )

    def __str__(self):
        return f"{self.user} - {self.type}"

    class Meta:
        db_table = "profile"
