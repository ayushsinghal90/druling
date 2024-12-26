from django.urls import path
from .views import RestaurantView

urlpatterns = [
    path("list/", RestaurantView.as_view({"get": "get_list"})),
]
