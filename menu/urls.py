from django.urls import path

from menu.views import QRMenuView

urlpatterns = [
    path("", QRMenuView.as_view()),
]
