from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RestaurantView

router = DefaultRouter()
router.register(r"", RestaurantView, basename="restaurants")

urlpatterns = [
    path("", include(router.urls)),
]
