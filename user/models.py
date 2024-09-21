from django.core.validators import RegexValidator
from django.db import models

from commons.models.BaseModel import BaseModel


class User(BaseModel):
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$", message="Enter a valid phone number."
            )
        ],
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password_hash = models.CharField(max_length=128)
    salt = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "user"
