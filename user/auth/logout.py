from rest_framework_simplejwt.tokens import RefreshToken

from commons.api.responses import ResponseFactory


def logout_user(request):
    try:
        refresh = request.data.get("refresh")
        RefreshToken(token=refresh).blacklist()
        return ResponseFactory.success(message="Logged out successfully")
    except Exception as e:
        print(e)
        return ResponseFactory.bad_request(message="Invalid token")
