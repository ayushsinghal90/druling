from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from plan.serializer import PlanGetSerializer
from plan.services import PlanService


class PlanView(ViewSet):
    def __init__(self, plan_service=None, **kwargs):
        super().__init__(**kwargs)
        self.plan_service = plan_service or PlanService()

    @api_handler()
    def get_all_plans(self, request):
        all_plans = self.plan_service.get_all_active_plans()
        return ResponseFactory.success(PlanGetSerializer(all_plans, many=True).data)

    @api_handler()
    def get_plan_by_id(self, request, plan_id):
        plan = self.plan_service.get_by_id(plan_id)
        return ResponseFactory.success(PlanGetSerializer(plan).data)

    @api_handler()
    def get_plan_by_details(self, request, product, plan_type):
        plan = self.plan_service.get_plan_by_details(product, plan_type)
        return ResponseFactory.success(PlanGetSerializer(plan).data)
