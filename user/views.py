from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from commons.middleware.api_handler import api_handler
from .auth.login import login_user
from .auth.logout import logout_user
from .auth.register import sign_up
from .auth.social_auth import google_login


class AuthView(ViewSet):
    permission_classes = (AllowAny,)

    @api_handler()
    def login(self, request):
        return login_user(request)

    @api_handler()
    def sign_up(self, request):
        return sign_up(request.data)

    @api_handler()
    def google_login(self, request):
        return google_login(request.data)


class LogoutView(ViewSet):
    @api_handler()
    def logout(self, request):
        return logout_user(request)
