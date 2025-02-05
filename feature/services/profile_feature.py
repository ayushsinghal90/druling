import logging

from commons.service.BaseService import BaseService
from ..models import ProfileFeature

logger = logging.getLogger(__name__)


class ProfileFeatureService(BaseService):
    def __init__(self):
        super().__init__(ProfileFeature)

    def create_subscription(self, plan_id, profile_id):
        return
