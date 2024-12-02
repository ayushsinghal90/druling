from ..serializers import UserSerializer


def generate_payload(user, refresh_token):
    return {
        "payload": UserSerializer(user).data,
        "refresh": str(refresh_token),
        "access": str(refresh_token.access_token),
    }
