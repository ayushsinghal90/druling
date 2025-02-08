import logging
from datetime import datetime, timedelta

from rest_framework.exceptions import ValidationError
from django.db import transaction

from commons.service.BaseService import BaseService
from feature.services import ProfileFeatureService
from plan.services import PlanService
from .enums import SubscriptionStatus
from .models import Subscription
from .serializer import SubscriptionCreateSerializer

logger = logging.getLogger(__name__)


class SubscriptionService(BaseService):
    def __init__(self, plan_service=None, profile_feature_service=None):
        super().__init__(Subscription)
        self.plan_service = plan_service or PlanService()
        self.profile_feature_service = (
            profile_feature_service or ProfileFeatureService()
        )

    def create_subscription(self, plan_id, profile_id):
        with transaction.atomic():
            self.validate_if_subscription_exists(profile_id)
            plan = self.plan_service.get_active_plan_by_id(plan_id)

            start_date = datetime.now().date()
            end_date = start_date + timedelta(days=plan.duration)

            subscription_serializer = SubscriptionCreateSerializer(
                data={
                    "profile_id": profile_id,
                    "plan_id": plan_id,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                partial=True,
            )
            if subscription_serializer.is_valid(raise_exception=True):
                return subscription_serializer.save()

    def update_status(self, status, id):
        with transaction.atomic():
            subscription = self.get_by_id(id)
            subscription.status = status
            subscription.save()

            if subscription.status == SubscriptionStatus.COMPLETED:
                self.profile_feature_service.update_subscription(
                    subscription.plan_id, subscription.profile_id
                )

            return subscription

    def get_by_profile_id(self, profile_id, statuses=None):
        if statuses is None:
            statuses = [SubscriptionStatus.IN_PROGRESS, SubscriptionStatus.COMPLETED]
        return self.model.objects.filter(profile_id=profile_id, status__in=statuses)

    def validate_if_subscription_exists(self, profile_id):
        if self.get_by_profile_id(
            profile_id,
            statuses=[SubscriptionStatus.IN_PROGRESS, SubscriptionStatus.DRAFT],
        ).exists():
            raise ValidationError("Subscription already active for this profile")
