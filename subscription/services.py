import logging
from datetime import datetime

from django.db import transaction

from commons.service.BaseService import BaseService
from subscription_plan.services import SubscriptionPlanService
from .models import Subscription
from .serializer import SubscriptionCreateSerializer

logger = logging.getLogger(__name__)


class SubscriptionService(BaseService):
    def __init__(self, plan_service=None):
        super().__init__(Subscription)
        self.plan_service = plan_service or SubscriptionPlanService()

    def create_subscription(self, plan_id, profile_id):
        with transaction.atomic():
            subscription_plan = self.plan_service.get_active_plan_by_id(plan_id)

            start_date = datetime.now().date()
            end_date = start_date.__add__(subscription_plan.duration)

            subscription_serializer = SubscriptionCreateSerializer(
                data={
                    "profile_id": profile_id,
                    "plan_id": plan_id,
                    "start_date": start_date,
                    "end_date": end_date,
                }
            )
            if subscription_serializer.is_valid(raise_exception=True):
                return subscription_serializer.save()

    def update_status(self, status, id):
        with transaction.atomic():
            subscription = self.get_by_id(id)
            subscription.status = status
            subscription.save()
            return subscription
