from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory

from ..serializers import RegisterSerializer
from .utils import generate_payload

User = get_user_model()


def sign_up(data):
    """
    Get or create a new user.
    """
    count = User.objects.filter(email=data["email"]).count()
    if count < 1:
        # If no user exists, create a new one
        serializer = RegisterSerializer(data=data)

        # Validate serializer
        if not serializer.is_valid():
            return ResponseFactory.bad_request(errors=serializer.errors)

        # Save the user and generate tokens
        serializer.save()

    user = User.objects.get(email=data["email"])
    refresh_token = RefreshToken.for_user(user)
    return ResponseFactory.created(
        data=generate_payload(user, refresh_token),
        message="User registered successfully",
    )
