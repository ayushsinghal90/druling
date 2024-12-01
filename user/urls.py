from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LoginUserView, RegisterUserView

router = DefaultRouter()
router.register(r"sign-up", RegisterUserView, basename="sign-up")
router.register(r"login", LoginUserView, basename="login")

urlpatterns = [
    path("", include(router.urls)),
]
