from ..serializers import UserProfileSerializer


def generate_payload(user, refresh_token):
    return {
        "profile": UserProfileSerializer(user).data,
        "refresh": str(refresh_token),
        "access": str(refresh_token.access_token),
    }
