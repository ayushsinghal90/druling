import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import CustomerFavourite

logger = logging.getLogger(__name__)


class CustomerFavouriteService(BaseService):
    def __init__(self):
        super().__init__(CustomerFavourite)

    def create(self):
        with transaction.atomic():
            return
