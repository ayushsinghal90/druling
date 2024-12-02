from django.db import models

from commons.models.BaseModel import BaseModel
from contact.models import Contact
from user.models import User


class Profile(BaseModel):
    PROFILE_TYPE = (
        ("manager", "Manager"),
        ("employee", "Employee"),
        ("admin", "Admin"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=PROFILE_TYPE)
    img_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Profile Image URL",
    )
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE, related_name="profile", null=True, blank=True
    )

    def __str__(self):
        return f"{self.user} - {self.type}"

    class Meta:
        db_table = "profile"
