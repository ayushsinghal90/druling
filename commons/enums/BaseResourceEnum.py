from enum import Enum
import os

env = os.getenv("ENV", "dev")


class BaseResourceEnum(Enum):
    def __str__(self):
        return f"${env}-{self.value}"

    @property
    def value(self) -> str:
        return super().value

    @classmethod
    def choices(cls):
        """Generate choices for use in Django models."""
        return [(item.value, item.name) for item in cls]
