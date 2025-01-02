from django.urls import path
from .views import ProfileView

urlpatterns = [
    path("update/", ProfileView.as_view({"post": "update_profile"})),
]
