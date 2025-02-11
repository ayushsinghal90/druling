import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import Feature
from ..serializer import FeatureGetSerializer, FeatureCreateSerializer

logger = logging.getLogger(__name__)


class FeatureService(BaseService):
    def __init__(self):
        super().__init__(Feature)

    def create(self, features, plan):
        with transaction.atomic():
            for feature in features:
                feature["plan"] = plan.id

            serializer = FeatureCreateSerializer(data=features, many=True)
            serializer.is_valid(raise_exception=True)

            feature_instances = [Feature(**data) for data in serializer.validated_data]

            features_saved = Feature.objects.bulk_create(feature_instances)

            return FeatureGetSerializer(features_saved, many=True).data

    def get_all(self, plan):
        try:
            return Feature.objects.filter(plan=plan, is_active=True)
        except Exception as e:
            logger.error(f"Error fetching features: {e}")
            return []
