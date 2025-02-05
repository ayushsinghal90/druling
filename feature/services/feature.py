import logging

from commons.service.BaseService import BaseService
from ..models import Feature

logger = logging.getLogger(__name__)


class FeatureService(BaseService):
    def __init__(self):
        super().__init__(Feature)

    def create_subscription(self, plan_id, profile_id):
        return
