from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory
from commons.clients import RedisClient
from commons.enums import RedisKey

from ..services import UserService
from .utils import generate_payload

user_service = UserService()


class RegisterService:
    def __init__(self, redis_client=None):
        self.redis_client = redis_client or RedisClient()

    def sign_up(self, data):
        """
        Get or create a new user.
        """
        is_verified = self.redis_client.get(
            f"{RedisKey.EMAIL_VERIFIED}:{data.get('email')}"
        )

        if not is_verified:
            return ResponseFactory.bad_request(message="Email is not verified.")

        self.redis_client.delete(f"{RedisKey.EMAIL_VERIFIED}:{data.get('email')}")
        data["is_email_verified"] = True

        user = user_service.get_or_create(data)
        refresh_token = RefreshToken.for_user(user)
        return ResponseFactory.created(
            data=generate_payload(user, refresh_token),
            message="User registered successfully",
        )
