from enum import Enum


class BaseEnum(Enum):
    def __str__(self):
        return self.value

    @property
    def value(self) -> str:
        return super().value
