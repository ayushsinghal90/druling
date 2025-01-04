from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from ..requests import SendVerifyCodeSerializer, VerifyCodeSerializer
from ..services import EmailVerifyService


class AuthView(ViewSet):
    permission_classes = (AllowAny,)

    def __init__(self, email_verify_service=None, **kwargs):
        super().__init__(**kwargs)
        self.email_verify_service = email_verify_service or EmailVerifyService()

    @api_handler(SendVerifyCodeSerializer)
    def send_code(self, request):
        self.email_verify_service.send_code(request.data)
        return ResponseFactory.success(message="Verification code sent successfully")

    @api_handler(VerifyCodeSerializer)
    def verify(self, request):
        if self.email_verify_service.verify(request.data):
            return ResponseFactory.success(message="Email verified successfully")
        return ResponseFactory.bad_request(message="Invalid verification code")
