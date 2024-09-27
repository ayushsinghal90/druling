from django.urls import include, path
from rest_framework.routers import DefaultRouter

from menu.views import QRMenuView

router = DefaultRouter()
router.register(r"qr", QRMenuView, basename="menu")

urlpatterns = [
    path("", include(router.urls)),
]
