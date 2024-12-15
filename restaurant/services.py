import logging

from rest_framework.exceptions import ValidationError

from .serializer import RestaurantCreateSerializer

logger = logging.getLogger(__name__)


class RestaurantService:
    def create(self, restaurant_data):
        try:
            restaurant_serializer = RestaurantCreateSerializer(data=restaurant_data)

            if restaurant_serializer.is_valid(raise_exception=True):
                restaurant = restaurant_serializer.save()
                return restaurant

        except ValidationError as e:
            logger.warning(f"Validation error while creating restaurant: {str(e)}")
            raise e
        except Exception as e:
            logger.error("Error while creating restaurant", exc_info=True)
            raise e
