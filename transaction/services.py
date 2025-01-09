import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from subscription.services import SubscriptionService
from subscription_plan.services import SubscriptionPlanService
from .enums import TransactionStatus
from .models import Transaction
from .serializer import TransactionCreateSerializer

logger = logging.getLogger(__name__)


class TransactionService(BaseService):
    def __init__(self, subscription_service=None, subscription_plan=None):
        super().__init__(Transaction)
        self.subscription_service = subscription_service or SubscriptionService()
        self.subscription_plan = subscription_plan or SubscriptionPlanService()

    def initiate_payment(self, data, profile_id):
        with transaction.atomic():
            plan_id = data.get("plan_id")
            subscription = self.subscription_service.create_subscription(
                plan_id, profile_id
            )

            transaction_serializer = TransactionCreateSerializer(
                data={
                    "subscription_id": subscription.id,
                    "amount": subscription.plan.amount,
                    "status": TransactionStatus.IN_PROGRESS,
                }
            )
            transaction_obj = None
            if transaction_serializer.is_valid(raise_exception=True):
                transaction_obj = transaction_serializer.save()

            return {"transaction_id": transaction_obj.id}
