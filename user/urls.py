from django.urls import path
from .views import AuthView

urlpatterns = [
    path("login/", AuthView.as_view({"post": "login"})),
    path("sign_up/", AuthView.as_view({"post": "sign_up"})),
    path("google_login/", AuthView.as_view({"post": "google_login"})),
]
