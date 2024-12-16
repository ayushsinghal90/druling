from profile.models import Profile

from django.db import models

from branch.models import Branch
from commons.models.BaseModel import BaseModel


class EntityRelation(BaseModel):
    ROLE_TYPE = (
        ("owner", "Owner"),
        ("manager", "Manager"),
        ("employee", "Employee"),
        ("admin", "Admin"),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="relations",
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_TYPE,
    )

    def __str__(self):
        return f"{self.branch.name} - {self.profile.user.email}: ({self.role})"

    class Meta:
        db_table = "entity_relation"
