import logging


from feature.enums import FeatureType
from feature.services import ProfileFeatureService

logger = logging.getLogger(__name__)


class Restriction:
    def __init__(self, profile_id: str, profile_feature_service=None):
        self.profile_id = profile_id
        self.profile_feature_service = (
            profile_feature_service or ProfileFeatureService()
        )
        self.features = self.profile_feature_service.get_all(self.profile_id)

    def check(self, feature_type: FeatureType):
        for feature in self.features:
            if (
                feature.type == feature_type
                and feature.is_active
                and feature.usage < feature.limit
            ):
                return
            else:
                raise Exception("Feature not available")

    def increment_usage(self, feature_type: FeatureType):
        self.check(feature_type)

        for feature in self.features:
            if (
                feature.type == feature_type
                and feature.is_active
                and feature.usage < feature.limit
            ):
                self.profile_feature_service.update_usage(feature.id)
