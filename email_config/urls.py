from django.urls import path
from .views import BlockedEmailView

urlpatterns = [
    path("ses_notification/", BlockedEmailView.as_view({"post": "ses_notification"})),
]
