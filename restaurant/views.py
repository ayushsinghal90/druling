from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory

from .serializer import RestaurantGetSerializer
from .services import RestaurantService


class RestaurantView(ViewSet):
    def __init__(self, restaurant_service=None, **kwargs):
        super().__init__(**kwargs)
        self.restaurant_service = restaurant_service or RestaurantService()

    @action(detail=False, methods=["get"], url_path="list")
    def get_list(self, request):
        try:
            profile_id = request.user.profile.id
            restaurants = self.restaurant_service.get_list(profile_id)
            return ResponseFactory.success(
                RestaurantGetSerializer(restaurants, many=True).data
            )
        except ValidationError as e:
            return ResponseFactory.bad_request(message=e.detail)
        except Exception as e:
            return ResponseFactory.server_error(message=str(e))
