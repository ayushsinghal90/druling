from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import handle_api_exceptions

from .serializer import RestaurantGetSerializer
from .services import RestaurantService


class RestaurantView(ViewSet):
    def __init__(self, restaurant_service=None, **kwargs):
        super().__init__(**kwargs)
        self.restaurant_service = restaurant_service or RestaurantService()

    @action(detail=False, methods=["get"], url_path="list")
    @handle_api_exceptions
    def get_list(self, request):
        profile_id = request.user.profile.id
        restaurants = self.restaurant_service.get_list(profile_id)
        return ResponseFactory.success(
            RestaurantGetSerializer(restaurants, many=True).data
        )
