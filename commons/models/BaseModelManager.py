from django.db import models


class BaseModelManager(models.Manager):
    def get_queryset(self):
        """Return only non-deleted records by default."""
        return super().get_queryset().filter(deleted_at__isnull=True)
