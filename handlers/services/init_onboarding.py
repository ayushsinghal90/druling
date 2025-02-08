import logging

from django.db import transaction

from constants.promotions import Promotions
from plan.services import PlanService
from profile.models import Profile
from subscription.enums import SubscriptionStatus
from subscription.services import SubscriptionService

logger = logging.getLogger(__name__)


class Onboarding:
    def __init__(
        self, profile: Profile, plan_service: None, subscription_service: None
    ):
        self.profile = profile
        self.plan_service = plan_service or PlanService()
        self.subscription_service = subscription_service or SubscriptionService()

    def run(self):
        self.init_promotions()

    def init_promotions(self):
        with transaction.atomic():
            for promotion in Promotions.NEW_USER:
                self.create_subscription(promotion["product"], promotion["plan"])

    def create_subscription(self, product, plan_type):
        with transaction.atomic():
            plan = self.plan_service.get_plan_by_details(product, plan_type)

            subscription = self.subscription_service.create_subscription(
                plan.id, self.profile.id
            )
            self.subscription_service.update_status(
                SubscriptionStatus.COMPLETED, subscription.id
            )
