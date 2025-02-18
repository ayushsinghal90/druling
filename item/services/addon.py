import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import Addon
from ..serializer import AddonSerializer

logger = logging.getLogger(__name__)


class AddonService(BaseService):
    def __init__(self):
        super().__init__(Addon)

    def create(self, data):
        with transaction.atomic():
            addon = AddonSerializer(data=data)
            if addon.is_valid(raise_exception=True):
                addon.save()
                return addon
