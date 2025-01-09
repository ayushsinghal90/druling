import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from subscription.enums import SubscriptionStatus
from subscription.services import SubscriptionService
from .enums import TransactionStatus
from .models import Transaction
from .serializer import TransactionCreateSerializer

logger = logging.getLogger(__name__)


class TransactionService(BaseService):
    def __init__(self, subscription_service=None):
        super().__init__(Transaction)
        self.subscription_service = subscription_service or SubscriptionService()

    def initiate_payment(self, data, profile_id):
        with transaction.atomic():
            plan_id = data.get("plan_id")
            subscription = self.subscription_service.create_subscription(
                plan_id, profile_id
            )

            transaction_serializer = TransactionCreateSerializer(
                data=self.create_transaction_data(subscription, profile_id, data),
                partial=True,
            )
            transaction_obj = None
            if transaction_serializer.is_valid(raise_exception=True):
                transaction_obj = transaction_serializer.save()

            return {"transaction_id": transaction_obj.id}

    def create_transaction_data(self, subscription, profile_id, data):
        subscription_plan = subscription.plan
        amount = subscription_plan.amount
        discount = data.get("discount", 0)

        total_amount = amount - discount

        return {
            "subscription_id": subscription.id,
            "status": TransactionStatus.PENDING.name,
            "amount": subscription_plan.amount,
            "profile_id": profile_id,
            "discount": discount,
            "taxes": 0,
            "total_amount": total_amount,
        }

    def update_transaction_status(self, status, id):
        with transaction.atomic():
            transaction_obj = self.get_by_id(id)
            subscription_status = SubscriptionStatus.IN_PROGRESS
            if status == "success":
                transaction_obj.status = TransactionStatus.COMPLETED
            else:
                transaction_obj.status = TransactionStatus.FAILED
                subscription_status = SubscriptionStatus.FAILED

            self.subscription_service.update_status(
                subscription_status, transaction_obj.subscription.id
            )
            transaction_obj.save()
            return transaction_obj
