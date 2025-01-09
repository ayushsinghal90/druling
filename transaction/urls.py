from django.urls import path
from .views import TransactionView

urlpatterns = [
    path("initiate/", TransactionView.as_view({"post": "initiate"})),
]
