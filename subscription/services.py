import logging

from commons.service.BaseService import BaseService
from .models import Subscription

logger = logging.getLogger(__name__)


class SubscriptionService(BaseService):
    def __init__(self):
        super().__init__(Subscription)

    def create(self, data):
        return None
