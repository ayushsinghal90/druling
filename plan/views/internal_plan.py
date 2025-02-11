from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from commons.middleware.internal_auth import (
    InternalTokenAuthentication,
    IsInternalRequest,
)
from plan.serializer import PlanGetSerializer, PlanCreateSerializer
from plan.services import PlanService


class InternalPlanView(ViewSet):
    authentication_classes = [InternalTokenAuthentication]
    permission_classes = [IsInternalRequest]

    def __init__(self, plan_service=None, **kwargs):
        super().__init__(**kwargs)
        self.plan_service = plan_service or PlanService()

    @api_handler(serializer=PlanCreateSerializer)
    def create_plan(self, request):
        plan = self.plan_service.create(request.data)
        return ResponseFactory.success(PlanGetSerializer(plan).data)
