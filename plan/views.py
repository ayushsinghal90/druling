from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from .serializer import PlanGetSerializer
from .services import PlanService


class PlanView(ViewSet):
    def __init__(self, subscription_plan_service=None, **kwargs):
        super().__init__(**kwargs)
        self.subscription_plan_service = subscription_plan_service or PlanService()

    @api_handler()
    def get_all_plans(self, request):
        all_plans = self.subscription_plan_service.get_all_active_plans()
        return ResponseFactory.success(PlanGetSerializer(all_plans, many=True).data)

    @api_handler()
    def get_plan_by_id(self, request, plan_id):
        plan = self.subscription_plan_service.get_by_id(plan_id)
        return ResponseFactory.success(PlanGetSerializer(plan).data)
