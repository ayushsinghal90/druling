from django.urls import path
from ..views import OrderView, OrderItemView

urlpatterns = [
    path("create/", OrderView.as_view({"post": "create"})),
    path("update-status/", OrderView.as_view({"post": "update_status"})),
    path("item/update-status/", OrderItemView.as_view({"post": "update_status"})),
]
