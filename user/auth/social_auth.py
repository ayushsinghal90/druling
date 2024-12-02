from django.contrib.auth import get_user_model
from google.auth.transport.requests import Request
from google.oauth2 import id_token
from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory

from .utils import generate_payload

User = get_user_model()


def google_login(data):
    token = data.get("token")  # Get the Google token from the front-end

    try:
        id_info = id_token.verify_oauth2_token(
            token, Request(), "your-google-client-id"
        )

        if (
            id_info["iss"] != "accounts.google.com"
            and id_info["iss"] != "https://accounts.google.com"
        ):
            raise ValueError("Wrong issuer.")

        user = get_user_model().objects.filter(email=id_info["email"]).first()
        if not user:
            user = get_user_model().objects.create_user(
                email=id_info["email"],
                first_name=id_info.get("given_name", ""),
                last_name=id_info.get("family_name", ""),
            )

        # Create JWT for the user
        refresh_token = RefreshToken.for_user(user)

        return ResponseFactory.success(
            data=generate_payload(user, refresh_token),
            message="Login successful",
        )
    except ValueError:
        return ResponseFactory.bad_request(message="Invalid token")
