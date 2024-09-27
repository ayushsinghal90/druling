import logging

from rest_framework.exceptions import ValidationError

from .serializer import BranchLocationSerializer

logger = logging.getLogger(__name__)


class BranchLocationService:
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
            raise e
