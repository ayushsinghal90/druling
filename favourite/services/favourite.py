import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import Favourite

logger = logging.getLogger(__name__)


class FavouriteService(BaseService):
    def __init__(self):
        super().__init__(Favourite)

    def create(self):
        with transaction.atomic():
            return
