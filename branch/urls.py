from django.urls import include, path
from rest_framework.routers import DefaultRouter

from branch.views import BranchView

router = DefaultRouter()
router.register(r"", BranchView, basename="branch")

urlpatterns = [
    path("", include(router.urls)),
]
