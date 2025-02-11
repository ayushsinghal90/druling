from rest_framework.viewsets import ViewSet

from ..services import FeatureService


class FeatureView(ViewSet):
    def __init__(self, feature_service=None, **kwargs):
        super().__init__(**kwargs)
        self.feature_service = feature_service or FeatureService()
