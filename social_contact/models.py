from django.db import models

from commons.models.BaseModel import BaseModel
from contact.models import Contact


class SocialContact(BaseModel):
    facebook = models.URLField(blank=True, null=True)
    x_link = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    contact = models.OneToOneField(
        Contact,
        related_name="socials",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"social {self.id}"

    class Meta:
        db_table = "social_contact"
