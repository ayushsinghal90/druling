import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import ValidationError

from branch_location.services import BranchLocationService
from commons.exceptions.BaseError import BaseError
from contact.services import ContactService
from entity_relation.services import EntityRelationService
from restaurant.services import RestaurantService

from .models import Branch
from .serializer import BranchCreateModelSerializer

logger = logging.getLogger(__name__)


class BranchService:
    def __init__(
        self,
        branch_location_service=None,
        restaurant_service=None,
        entity_relation_service=None,
        contact_service=None,
    ):
        self.branch_location_service = (
            branch_location_service or BranchLocationService()
        )
        self.restaurant_service = restaurant_service or RestaurantService()
        self.entity_relation_service = (
            entity_relation_service or EntityRelationService()
        )
        self.contact_service = contact_service or ContactService()

    def create(self, branch_data, profile_id):
        with transaction.atomic():
            # Validate input data
            branch = branch_data.get("branch")
            restaurant_id = branch_data.get("restaurant_id")
            restaurant_data = branch_data.get("restaurant")
            branch_location_data = branch_data.get("branch_location")
            contact_data = branch_data.get("contact")

            contact = self.contact_service.get_or_create(contact_data)
            restaurant_data["contact_id"] = contact.id

            # Create or retrieve restaurant
            restaurant = self._get_or_create_restaurant(restaurant_id, restaurant_data)

            # Create branch location
            branch_location = self._create_branch_location(branch_location_data)

            # Create branch
            branch["contact_id"] = contact.id
            branch["restaurant_id"] = restaurant.id
            branch["location_id"] = branch_location.id

            branch_instance = self._create_branch(branch, profile_id)

            return branch_instance

    def _get_or_create_restaurant(self, restaurant_id, restaurant_data):
        """Retrieve an existing restaurant or create a new one."""
        if restaurant_id:
            restaurant = self.restaurant_service.get_by_id(restaurant_id)
            if not restaurant:
                raise ValidationError(
                    f"Restaurant with ID {restaurant_id} does not exist"
                )
        else:
            restaurant = self.restaurant_service.create(restaurant_data)
        return restaurant

    def _create_branch_location(self, branch_location_data):
        """Create a branch location."""
        return self.branch_location_service.create(branch_location_data)

    def _create_branch(self, branch, profile_id):
        """Validate and save the branch."""
        branch_serializer = BranchCreateModelSerializer(data=branch)
        if branch_serializer.is_valid(raise_exception=True):
            branch_instance = branch_serializer.save()
            self.entity_relation_service.create_relation(branch_instance.id, profile_id)
            return branch_instance

    def get_branch_by_id(self, branch_id):
        try:
            return Branch.objects.get(id=branch_id)
        except Branch.DoesNotExist:
            logger.error(f"Branch with ID {branch_id} does not exist.")
            raise ObjectDoesNotExist(f"Branch with ID {branch_id} does not exist.")

        except Exception as e:
            logger.error(
                f"An error occurred while fetching the branch: {str(e)}", exc_info=True
            )
            raise BaseError("Error while fetching the branch", original_exception=e)
