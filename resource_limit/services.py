import logging

from commons.service.BaseService import BaseService
from .models import ResourceLimit

logger = logging.getLogger(__name__)


class ResourceLimitService(BaseService):
    def __init__(self):
        super().__init__(ResourceLimit)

    def create(self, data):
        return None
