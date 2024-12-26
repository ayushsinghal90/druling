from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from .requests import BranchCreateSerializer, BranchEditSerializer

from .serializer import BranchGetModelSerializer
from .services import BranchService


class BranchView(ViewSet):
    def __init__(self, branch_service=None, **kwargs):
        super().__init__(**kwargs)
        self.branch_service = branch_service or BranchService()

    @action(detail=False, methods=["post"], url_path="create")
    @api_handler(serializer=BranchCreateSerializer)
    def create_branch(self, request):
        profile_id = request.user.profile.id
        branch = self.branch_service.create(request.data, profile_id)
        return ResponseFactory.created(BranchGetModelSerializer(branch).data)

    @action(detail=True, methods=["put"])
    @api_handler(serializer=BranchEditSerializer)
    def update_branch(self, request, branch_id=None):
        branch = self.branch_service.update(branch_id, request.data)
        return ResponseFactory.success(BranchGetModelSerializer(branch).data)
