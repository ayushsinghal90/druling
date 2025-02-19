from django.urls import path
from ..views import SeatView

urlpatterns = [
    path("create/", SeatView.as_view({"post": "create"})),
]
