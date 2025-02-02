from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from .services import BlockedEmailService


@method_decorator(csrf_exempt, name="dispatch")
class BlockedEmailView(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self, blocked_email_service=None, **kwargs):
        super().__init__(**kwargs)
        self.blocked_email_service = blocked_email_service or BlockedEmailService()

    def ses_notification(self, request):
        self.blocked_email_service.process_notification(request.data)
        return ResponseFactory.success()
