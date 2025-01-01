from django.urls import path
from .views import AuthView, LogoutView

urlpatterns = [
    path("login/", AuthView.as_view({"post": "login"})),
    path("sign_up/", AuthView.as_view({"post": "sign_up"})),
    path("google_login/", AuthView.as_view({"post": "google_login"})),
    path("logout/", LogoutView.as_view({"post": "logout"})),
]
