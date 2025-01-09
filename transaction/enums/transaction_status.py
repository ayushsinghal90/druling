from commons.enums.BaseEnum import BaseEnum


class TransactionStatus(BaseEnum):
    COMPLETED = "completed"
    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
