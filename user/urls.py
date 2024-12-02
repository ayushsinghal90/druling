from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthView

router = DefaultRouter()
router.register(r"", AuthView, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
]
