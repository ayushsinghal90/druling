from django.urls import path
from .views import PlanView, InternalPlanView

urlpatterns = [
    path("all/", PlanView.as_view({"get": "get_all_plans"})),
    path("<plan_id>/", PlanView.as_view({"get": "get_plan_by_id"})),
    path("<product>/<plan_type>/", PlanView.as_view({"get": "get_plan_by_details"})),
    path("create/", InternalPlanView.as_view({"post": "create_plan"})),
]
