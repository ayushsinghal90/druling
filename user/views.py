from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory

from .serializers import RegisterSerializer


class LoginUserView(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"], url_path="/")
    def login(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return ResponseFactory.bad_request(errors=serializer.errors)
        serializer.save()

        user = User.objects.get(username=request.data["username"])
        refresh = RefreshToken.for_user(user)
        return ResponseFactory.created(
            data={
                "payload": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            message="User created",
        )


class RegisterUserView(ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"], url_path="/")
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return ResponseFactory.bad_request(errors=serializer.errors)
        serializer.save()

        user = User.objects.get(username=request.data["username"])
        refresh = RefreshToken.for_user(user)
        return ResponseFactory.created(
            data={
                "payload": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            message="User created",
        )
