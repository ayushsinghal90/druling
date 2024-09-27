from django.urls import path

from branch.views import BranchView

urlpatterns = [
    path("", BranchView.as_view()),
]
