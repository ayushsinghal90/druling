from django.urls import path
from .views import QRMenuView

urlpatterns = [
    path("create/", QRMenuView.as_view({"post": "create_menu"})),
]
