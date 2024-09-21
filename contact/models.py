from django.db import models

from commons.models.BaseModel import BaseModel


class Contact(BaseModel):
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        contact_str = f"Email: {self.email}" if self.email else ""
        if self.phone_number:
            contact_str += f" | Phone: {self.phone_number}"
        return contact_str if contact_str else "No Contact Info"

    class Meta:
        db_table = "contact"
