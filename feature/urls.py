from django.urls import path
from .views import ProfileFeatureView

urlpatterns = [
    path("profile/all/", ProfileFeatureView.as_view({"get": "get_all"})),
]
