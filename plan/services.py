import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from feature.services import FeatureService
from .models import Plan
from .serializer import PlanCreateSerializer

logger = logging.getLogger(__name__)


class PlanService(BaseService):
    def __init__(self, feature_service=None):
        super().__init__(Plan)
        self.feature_service = feature_service or FeatureService()

    def create(self, data):
        with transaction.atomic():
            plan_data = data.get("plan")

            serializer = PlanCreateSerializer(data=plan_data)
            serializer.is_valid(raise_exception=True)

            plan = serializer.save()

            features = data.get("features")
            self.feature_service.create(features, plan)
            return plan

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

    def get_all_active_plans(self):
        return self.model.objects.filter(is_active=True)

    def get_plan_by_details(self, product=None, plan_type=None):
        try:
            return self.model.objects.get(product=product, plan_type=plan_type)
        except self.model.DoesNotExist:
            logger.error(
                f"{self.model.__name__} with product {product} and plan_type {plan_type} does not exist."
            )
            raise ObjectDoesNotExist(
                f"{self.model.__name__} with product {product} and plan_type {plan_type} does not exist."
            )

        except Exception as e:
            logger.error(
                f"An error occurred while fetching the {self.model.__name__}: {str(e)}",
                exc_info=True,
            )
            raise BaseError(
                f"Error while fetching the {self.model.__name__}", original_exception=e
            )
