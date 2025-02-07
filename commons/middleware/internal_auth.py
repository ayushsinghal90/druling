from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from rest_framework.permissions import BasePermission


class InternalTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Internal-Token")
        if not token:
            return None

        if token != settings.INTERNAL_API_TOKEN:
            raise AuthenticationFailed("Invalid token")

        return None, None


class IsInternalRequest(BasePermission):
    def has_permission(self, request, view):
        return request.auth is None and request.user is None
