from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


class LoginUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is None:
            return ResponseFactory.unauthorized(message="Invalid credentials")

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        return ResponseFactory.success(
            data={
                "payload": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            message="Login successful",
        )


class RegisterUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        # Validate serializer
        if not serializer.is_valid():
            return ResponseFactory.bad_request(errors=serializer.errors)

        # Save the user and generate tokens
        serializer.save()
        user = User.objects.get(email=request.data["email"])
        refresh = RefreshToken.for_user(user)
        return ResponseFactory.created(
            data={
                "payload": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            message="User registered successfully",
        )
