import logging

from commons.service.BaseService import BaseService
from .models import Transaction

logger = logging.getLogger(__name__)


class TransactionService(BaseService):
    def __init__(self):
        super().__init__(Transaction)

    def create(self, data):
        return None
