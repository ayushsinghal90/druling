import logging

from django.db.models import Prefetch
from rest_framework.exceptions import ValidationError

from branch.models import Branch
from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService

from .models import Restaurant
from .serializer import RestaurantCreateSerializer

logger = logging.getLogger(__name__)


class RestaurantService(BaseService):
    def __init__(self):
        super().__init__(Restaurant)

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
            raise BaseError("Error while creating restaurant", original_exception=e)

    def get_list(self, profile_id):
        try:
            return self._get_restaurants_with_branches(profile_id)
        except Exception as e:
            logger.error("Error while fetching restaurant", exc_info=True)
            raise BaseError("Error while fetching restaurant", original_exception=e)

    def _get_restaurants_with_branches(self, profile_id):
        return (
            Restaurant.objects.filter(branches__relations__profile_id=profile_id)
            .prefetch_related(
                Prefetch(
                    "branches",
                    queryset=Branch.objects.filter(relations__profile_id=profile_id),
                )
            )
            .distinct()
        )
