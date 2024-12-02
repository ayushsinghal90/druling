from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory

from .utils import generate_payload

User = get_user_model()


def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    # Authenticate user
    user = authenticate(request, username=email, password=password)

    if user is None:
        return ResponseFactory.unauthorized(message="Invalid credentials")

    # Generate tokens
    refresh_token = RefreshToken.for_user(user)
    return ResponseFactory.success(
        data=generate_payload(user, refresh_token),
        message="Login successful",
    )
