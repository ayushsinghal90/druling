from django.urls import path
from .views import RestaurantView

urlpatterns = [
    path("list/", RestaurantView.as_view({"get": "get_list"})),
    path("<restaurant_id>/", RestaurantView.as_view({"get": "get_restaurant_by_id"})),
]
