from django.db import models

from commons.models.BaseModel import BaseModel
from profile.models import Profile
from ..enums import FeatureType


class ProfileFeature(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=50,
        choices=[(type.name, type.value) for type in FeatureType],
    )
    limit = models.IntegerField(default=0)
    usage = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.type}"

    class Meta:
        db_table = "profile_feature"
