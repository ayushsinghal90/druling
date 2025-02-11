import logging

from django.core.exceptions import ObjectDoesNotExist

from commons.exceptions.BaseError import BaseError

logger = logging.getLogger(__name__)


class BaseService:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id, filters=None):
        try:
            query = self.model.objects.filter(id=id)
            if filters:
                query = query.filter(**filters)
            return query.get()
        except self.model.DoesNotExist:
            logger.error(f"{self.model.__name__} with ID {id} does not exist.")
            raise ObjectDoesNotExist(
                f"{self.model.__name__} with ID {id} does not exist."
            )
        except Exception as e:
            logger.error(
                f"An error occurred while fetching the {self.model.__name__}: {str(e)}",
                exc_info=True,
            )
            raise BaseError(
                f"Error while fetching the {self.model.__name__}", original_exception=e
            )
