import logging

from commons.service.BaseService import BaseService
from .models import SubscriptionPlan

logger = logging.getLogger(__name__)


class SubscriptionPlanService(BaseService):
    def __init__(self):
        super().__init__(SubscriptionPlan)

    def create(self, data):
        return None
