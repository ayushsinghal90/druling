from commons.enums.BaseEnum import BaseEnum


class SubscriptionStatus(BaseEnum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    CANCELLED = "cancelled"
    FAILED = "failed"
