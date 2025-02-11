from enum import Enum
from django.conf import settings


env = settings.ENV


class BaseResourceEnum(Enum):
    def __str__(self):
        base = f"{env}-" if env else ""
        return f"{base}{self.value}"

    @property
    def value(self) -> str:
        base = f"{env}-" if env else ""
        return f"{base}{super().value}"

    @classmethod
    def choices(cls):
        """Generate choices for use in Django models."""
        return [(item.value, item.name) for item in cls]
