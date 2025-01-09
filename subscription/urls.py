from django.urls import path
from .views import SubscriptionView

urlpatterns = [
    path("all/", SubscriptionView.as_view({"get": "get_all_subscription"})),
    path("<subscription_id>/", SubscriptionView.as_view({"get": "get_by_id"})),
]
