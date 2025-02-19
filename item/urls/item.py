from django.urls import path
from ..views import ItemView

urlpatterns = [
    path("create/", ItemView.as_view({"post": "create"})),
]
