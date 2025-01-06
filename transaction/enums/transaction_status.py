from commons.enums.BaseEnum import BaseEnum


class TransactionStatus(BaseEnum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    CANCELLED = "cancelled"
    FAILED = "failed"
