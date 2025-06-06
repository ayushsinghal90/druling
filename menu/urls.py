from django.urls import path
from .views import QRMenuView, QRMenuPublicView

urlpatterns = [
    path("qr/create/", QRMenuView.as_view({"post": "create_menu"})),
    path("qr/<menu_id>/", QRMenuPublicView.as_view({"get": "get_menu_by_id"})),
    path(
        "qr/branch/<branch_id>/", QRMenuView.as_view({"get": "get_menu_by_branch_id"})
    ),
    path("qr/", QRMenuView.as_view({"get": "get_all"})),
]
