from django.urls import path
from .views import TransactionView

urlpatterns = [
    path("initiate/", TransactionView.as_view({"post": "initiate"})),
    path("all/", TransactionView.as_view({"get": "get_all"})),
]
