from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory

from ..services import UserService
from .utils import generate_payload

user_service = UserService()


def sign_up(data):
    """
    Get or create a new user.
    """
    user = user_service.get_or_create(data)
    refresh_token = RefreshToken.for_user(user)
    return ResponseFactory.created(
        data=generate_payload(user, refresh_token),
        message="User registered successfully",
    )
