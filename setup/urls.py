from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/", include("social_django.urls", namespace="social")),
    path(
        "api/",
        include(
            [
                path("user/", include("user.urls")),  # Prefix user URLs
                path("restaurant/", include("restaurant.urls")),
                path("branch/", include("branch.urls")),  # Added a prefix for branch
                path("item/", include("item.urls")),
                path(
                    "branch-location/", include("branch_location.urls")
                ),  # Hyphen used
                path("menu/", include("menu.urls")),
                path(
                    "entity-relation/", include("entity_relation.urls")
                ),  # Hyphen used
            ]
        ),
    ),
]
