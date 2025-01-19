from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler


class HealthCheckView(ViewSet):
    permission_classes = [AllowAny]

    @api_handler()
    def health_check(self, request):
        return ResponseFactory.success("Health check is successful")
