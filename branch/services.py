import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import ValidationError

from branch_location.services import BranchLocationService
from restaurant.services import RestaurantService

from .models import Branch
from .serializer import BranchCreateSerializer

logger = logging.getLogger(__name__)


class BranchService:
    def __init__(self, branch_location_service=None, restaurant_service=None):
        self.branch_location_service = (
            branch_location_service or BranchLocationService()
        )
        self.restaurant_service = restaurant_service or RestaurantService()

    def create(self, branch_data):
        try:
            with transaction.atomic():
                branch = branch_data.get("branch")
                restaurant_data = branch_data.get("restaurant")
                branch_location_data = branch_data.get("branch_location")

                if not branch or not restaurant_data or not branch_location_data:
                    raise ValidationError(
                        "Branch, restaurant, or branch location data missing"
                    )

                restaurant = self.restaurant_service.create(restaurant_data)
                branch_location = self.branch_location_service.create(
                    branch_location_data
                )

                branch["restaurant_id"] = restaurant.id
                branch["location_id"] = branch_location.id

                branch_serializer = BranchCreateSerializer(data=branch)
                if branch_serializer.is_valid(raise_exception=True):
                    branch_instance = branch_serializer.save()
                    return branch_instance

        except ValidationError as e:
            logger.warning(f"Validation error: {str(e)}")
            raise e
        except Exception as e:
            logger.e("Error while creating branch", exc_info=True)
            raise e

    def get_branch_by_id(self, branch_id):
        try:
            # Fetch the branch object from the database by ID
            branch = Branch.objects.get(id=branch_id)

            # Serialize the branch object
            branch_serializer = BranchCreateSerializer(branch)

            # Return the serialized data
            return branch_serializer.data

        except Branch.DoesNotExist:
            # Log and handle the case where the branch does not exist
            logger.error(f"Branch with ID {branch_id} does not exist.")
            raise ObjectDoesNotExist(f"Branch with ID {branch_id} does not exist.")

        except Exception as e:
            # Log any other exceptions that might occur
            logger.error(
                f"An error occurred while fetching the branch: {str(e)}", exc_info=True
            )
            raise e
