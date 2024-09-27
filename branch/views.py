from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from commons.api.responses import ResponseFactory

from .serializer import BranchSerializer
from .services import BranchService


class BranchCreateView(APIView):
    @action(detail=True, methods=["post"])
    def create(self, request):
        branch_service = BranchService()
        try:
            branch = branch_service.create(request.data)
            return ResponseFactory.created(BranchSerializer(branch).data)
        except ValidationError as e:
            return ResponseFactory.bad_request(e)
        except Exception:
            return ResponseFactory.server_error()
