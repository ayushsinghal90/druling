from django.urls import path
from .views import PlanView

urlpatterns = [
    path("all/", PlanView.as_view({"get": "get_all_plans"})),
    path("<plan_id>/", PlanView.as_view({"get": "get_plan_by_id"})),
]
