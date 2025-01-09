from enum import Enum


class BaseEnum(Enum):
    def __str__(self):
        return self.value

    @property
    def value(self) -> str:
        return super().value

    @classmethod
    def choices(cls):
        """Generate choices for use in Django models."""
        return [(item.value, item.name) for item in cls]
