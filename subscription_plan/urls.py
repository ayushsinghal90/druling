from django.urls import path
from .views import SubscriptionPlanView

urlpatterns = [
    path("all/", SubscriptionPlanView.as_view({"get": "get_all_plans"})),
    path("<plan_id>/", SubscriptionPlanView.as_view({"get": "get_plan_by_id"})),
]
