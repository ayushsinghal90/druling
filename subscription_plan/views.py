from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from subscription_plan.serializer import SubscriptionPlanGetSerializer
from subscription_plan.services import SubscriptionPlanService


class SubscriptionPlanView(ViewSet):
    def __init__(self, subscription_plan_service=None, **kwargs):
        super().__init__(**kwargs)
        self.subscription_plan_service = (
            subscription_plan_service or SubscriptionPlanService()
        )

    @api_handler()
    def get_all_plans(self, request):
        all_plans = self.subscription_plan_service.get_all_active_plans()
        return ResponseFactory.created(
            SubscriptionPlanGetSerializer(all_plans, many=True).data
        )

    @api_handler()
    def get_plan_by_id(self, request, plan_id):
        plan = self.subscription_plan_service.get_by_id(plan_id)
        return ResponseFactory.created(SubscriptionPlanGetSerializer(plan).data)
