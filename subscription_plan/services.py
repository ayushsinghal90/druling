import logging

from django.core.exceptions import ObjectDoesNotExist

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from .models import SubscriptionPlan

logger = logging.getLogger(__name__)


class SubscriptionPlanService(BaseService):
    def __init__(self):
        super().__init__(SubscriptionPlan)

    def get_active_plan_by_id(self, plan_id):
        try:
            return self.model.objects.get(id=plan_id, is_active=True)
        except self.model.DoesNotExist:
            logger.error(f"{self.model.__name__} with ID {plan_id} does not exist.")
            raise ObjectDoesNotExist(
                f"{self.model.__name__} with ID {plan_id} does not exist."
            )

        except Exception as e:
            logger.error(
                f"An error occurred while fetching the {self.model.__name__}: {str(e)}",
                exc_info=True,
            )
            raise BaseError(
                f"Error while fetching the {self.model.__name__}", original_exception=e
            )
