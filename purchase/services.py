import logging

from commons.service.BaseService import BaseService
from .models import Purchase

logger = logging.getLogger(__name__)


class PurchaseService(BaseService):
    def __init__(self):
        super().__init__(Purchase)

    def create(self, data):
        return None
