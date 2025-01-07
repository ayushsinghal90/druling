from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from commons.api.responses import ResponseFactory


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")

        try:
            # Verify token format and signature
            token = RefreshToken(refresh_token)
            user_id = token.payload.get("user_id")

            # Check if user exists and is active
            user = get_user_model().objects.filter(id=user_id).first()

            if not user:
                return ResponseFactory.unauthorized(message="User not found")

            if not user.is_active:
                return ResponseFactory.unauthorized(message="User account is disabled")

            return super().post(request, *args, **kwargs)

        except Exception as e:
            raise InvalidToken(str(e))
