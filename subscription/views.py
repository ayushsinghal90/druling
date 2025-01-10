from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from .serializer import SubscriptionGetSerializer
from .services import SubscriptionService


class SubscriptionView(ViewSet):
    def __init__(self, subscription_service=None, **kwargs):
        super().__init__(**kwargs)
        self.subscription_service = subscription_service or SubscriptionService()

    @api_handler()
    def get_all_subscription(self, request):
        profile_id = request.user.profile.id
        subscriptions = self.subscription_service.get_by_profile_id(profile_id)
        return ResponseFactory.success(
            SubscriptionGetSerializer(subscriptions, many=True).data
        )

    @api_handler()
    def get_by_id(self, request, subscription_id):
        plan = self.subscription_service.get_by_id(subscription_id)
        return ResponseFactory.success(SubscriptionGetSerializer(plan).data)
