from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from profile.requests import ProfileSerializer
from profile.serializer import ProfileGetSerializer
from profile.services import ProfileService


class ProfileView(ViewSet):
    def __init__(self, profile_service=None, **kwargs):
        super().__init__(**kwargs)
        self.profile_service = profile_service or ProfileService()

    @api_handler(serializer=ProfileSerializer)
    def update_profile(self, request):
        profile_id = request.user.profile.id
        profile = self.profile_service.update(profile_id, request.data)
        return ResponseFactory.success(ProfileGetSerializer(profile).data)
