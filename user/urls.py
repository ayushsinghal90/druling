from django.urls import path

from .views import RegisterUserView, UserDetailView

urlpatterns = [
    path("get-details", UserDetailView.as_view()),
    path("sign-up", RegisterUserView.as_view()),
]
