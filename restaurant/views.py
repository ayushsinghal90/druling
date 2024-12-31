from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler

from .serializer import RestaurantGetSerializer
from .services import RestaurantService


class RestaurantView(ViewSet):
    def __init__(self, restaurant_service=None, **kwargs):
        super().__init__(**kwargs)
        self.restaurant_service = restaurant_service or RestaurantService()

    @api_handler()
    def get_list(self, request):
        profile_id = request.user.profile.id
        restaurants = self.restaurant_service.get_list(profile_id)
        return ResponseFactory.success(
            RestaurantGetSerializer(restaurants, many=True).data
        )

    @api_handler()
    def get_restaurant_by_id(self, request, restaurant_id):
        restaurant = self.restaurant_service.get_by_id(restaurant_id)
        return ResponseFactory.created(RestaurantGetSerializer(restaurant).data)
