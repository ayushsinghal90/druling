from commons.enums.BaseEnum import BaseEnum


class OrderStatus(BaseEnum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
