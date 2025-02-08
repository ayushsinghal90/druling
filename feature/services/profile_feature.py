import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from . import FeatureService
from ..models import ProfileFeature
from ..serializer import ProfileFeatureCreateSerializer

logger = logging.getLogger(__name__)


class ProfileFeatureService(BaseService):
    def __init__(self, feature_service=None):
        super().__init__(ProfileFeature)
        self.feature_service = feature_service or FeatureService()

    def create_subscription(self, plan_id, profile_id):
        with transaction.atomic():
            features = self.feature_service.get_all_features(plan_id)

            profile_features = [
                {"profile_id": profile_id, "type": feature.type, "limit": feature.limit}
                for feature in features
            ]

            serializer = ProfileFeatureCreateSerializer(
                data=profile_features, many=True
            )
            serializer.is_valid(raise_exception=True)

            profile_feature_instances = [
                ProfileFeature(**data) for data in serializer.validated_data
            ]
            profile_features_saved = ProfileFeature.objects.bulk_create(
                profile_feature_instances
            )

            return profile_features_saved

    def get_all(self, profile_id):
        try:
            return ProfileFeature.objects.filter(profile=profile_id, is_active=True)
        except Exception as e:
            logger.error(f"Error fetching profile features: {e}")
            return []
