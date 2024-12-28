from django.urls import path
from .views import QRMenuView

urlpatterns = [
    path("qr/create/", QRMenuView.as_view({"post": "create_menu"})),
    path("qr/upload_url/", QRMenuView.as_view({"get": "get_menu_upload_url"})),
]
