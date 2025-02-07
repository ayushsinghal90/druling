from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from .serializer import PlanGetSerializer, PlanCreateSerializer
from .services import PlanService


class PlanView(ViewSet):
    def __init__(self, plan_service=None, **kwargs):
        super().__init__(**kwargs)
        self.plan_service = plan_service or PlanService()

    @api_handler(serializer=PlanCreateSerializer)
    def create_plan(self, request):
        plan = self.plan_service.create(request.data)
        return ResponseFactory.success(PlanGetSerializer(plan).data)

    @api_handler()
    def get_all_plans(self, request):
        all_plans = self.plan_service.get_all_active_plans()
        return ResponseFactory.success(PlanGetSerializer(all_plans, many=True).data)

    @api_handler()
    def get_plan_by_id(self, request, plan_id):
        plan = self.plan_service.get_by_id(plan_id)
        return ResponseFactory.success(PlanGetSerializer(plan).data)
