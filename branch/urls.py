from django.urls import path
from .views import BranchView

urlpatterns = [
    path("create/", BranchView.as_view({"post": "create_branch"})),
    path("<branch_id>/", BranchView.as_view({"put": "update_branch"})),
    path("<branch_id>/", BranchView.as_view({"get": "get_branch_by_id"})),
]
