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
            addon.is_valid(raise_exception=True)
            return addon.save()

    def bulk_create(self, data):
        with transaction.atomic():
            addon_serializer = AddonSerializer(data=data, many=True)
            addon_serializer.is_valid(raise_exception=True)

            addon_instances = [
                Addon(**data) for data in addon_serializer.validated_data
            ]
            addon_saved = Addon.objects.bulk_create(addon_instances)

            return addon_saved
