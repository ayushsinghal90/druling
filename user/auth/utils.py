from profile.serializer import ProfileGetSerializer


def generate_payload(user, refresh_token):
    return {
        "profile": ProfileGetSerializer(user.profile).data,
        "refresh": str(refresh_token),
        "access": str(refresh_token.access_token),
    }
