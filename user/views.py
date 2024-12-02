from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from .auth.login import login_user
from .auth.register import sign_up
from .auth.social_auth import google_login


class AuthView(ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        return login_user(request)

    @action(detail=False, methods=["post"], url_path="sign-up")
    def sign_up(self, request):
        return sign_up(request.data)

    @action(detail=False, methods=["post"], url_path="google-login")
    def google_login(self, request):
        return google_login(request.data)
