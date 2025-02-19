import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import ItemVariation
from ..serializer import ItemVariationSerializer

logger = logging.getLogger(__name__)


class ItemVariationService(BaseService):
    def __init__(self):
        super().__init__(ItemVariation)

    def create(self, item_id, data):
        with transaction.atomic():
            item_variation = ItemVariationSerializer(data=data)
            if item_variation.is_valid(raise_exception=True):
                item_variation.save(item_id=item_id)
                return item_variation

    def bulk_create(self, item_id, data):
        with transaction.atomic():
            for variation in data:
                variation["item_id"] = item_id

            item_variations = ItemVariationSerializer(data=data, many=True)
            item_variations.is_valid(raise_exception=True)

            variations_instances = [
                ItemVariation(**data) for data in item_variations.validated_data
            ]
            item_variations_saved = ItemVariation.objects.bulk_create(
                variations_instances
            )

            return item_variations_saved
