import logging

from rest_framework.exceptions import ValidationError

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from .models import BranchLocation
from .serializer import BranchLocationSerializer

logger = logging.getLogger(__name__)


class BranchLocationService(BaseService):
    def __init__(self):
        super().__init__(BranchLocation)

    def create(self, branch_location_data):
        try:
            branch_location_serializer = BranchLocationSerializer(
                data=branch_location_data
            )

            if branch_location_serializer.is_valid(raise_exception=True):
                branch_location = branch_location_serializer.save()
                return branch_location

        except ValidationError as e:
            logger.warning(f"Validation error while creating branch location: {str(e)}")
            raise e
        except Exception as e:
            logger.error("Error while creating branch location", exc_info=True)
            raise BaseError(
                "Error while creating branch location", original_exception=e
            )

    def update(self, id, branch_location_data):
        try:
            branch_location = self.get_by_id(id)

            branch_location_serializer = BranchLocationSerializer(
                branch_location, data=branch_location_data, partial=True
            )

            if branch_location_serializer.is_valid(raise_exception=True):
                branch_location = branch_location_serializer.save()
                return branch_location

        except ValidationError as e:
            logger.warning(f"Validation error while updating branch location: {str(e)}")
            raise e
        except Exception as e:
            logger.error("Error while updating branch location", exc_info=True)
            raise BaseError(
                "Error while updating branch location", original_exception=e
            )
