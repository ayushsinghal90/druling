from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from ..serializer import FeatureGetSerializer
from ..services import FeatureService


class FeatureView(ViewSet):
    def __init__(self, feature_service=None, **kwargs):
        super().__init__(**kwargs)
        self.feature_service = feature_service or FeatureService()

    @api_handler()
    def get_all_subscription(self, request):
        profile_id = request.user.profile.id
        feature = self.feature_service.get_by_profile_id(profile_id)
        return ResponseFactory.success(FeatureGetSerializer(feature, many=True).data)
