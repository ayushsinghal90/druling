from commons.enums.BaseEnum import BaseEnum


class SubscriptionStatus(BaseEnum):
    DRAFT = "draft"
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
