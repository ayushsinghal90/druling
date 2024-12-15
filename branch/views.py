from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory

from .serializer import BranchGetSerializer
from .services import BranchService


class BranchView(ViewSet):
    @action(detail=False, methods=["post"], url_path="create")
    def create_branch(self, request):
        branch_service = BranchService()
        try:
            profile_id = request.user.profile_id
            branch = branch_service.create(request.data, profile_id)
            return ResponseFactory.created(BranchGetSerializer(branch).data)
        except ValidationError:
            return ResponseFactory.bad_request()
        except Exception:
            return ResponseFactory.server_error()
