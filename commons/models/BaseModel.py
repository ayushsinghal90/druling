import uuid

from django.db import models
from django.db.models import Index
from django.utils import timezone

from commons.models.BaseModelManager import BaseModelManager


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Set the default manager to exclude soft-deleted objects
    objects = BaseModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
        indexes = [
            # Explicitly define an index for the deleted_at field
            Index(fields=["deleted_at"]),
        ]

    """Perform a soft delete by setting the deleted_at field."""

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    """Restore a soft-deleted record by clearing the deleted_at field."""

    def restore(self):
        self.deleted_at = None
        self.save()

    """Perform a hard delete by permanently removing the record from the database."""

    def hard_delete(self, using=None, keep_parents=False):
        super(BaseModel, self).delete(using=using, keep_parents=keep_parents)
