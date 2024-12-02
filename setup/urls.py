from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/",
        include(
            [
                path("", include("user.urls")),
                path("restaurant/", include("restaurant.urls")),
                path("", include("branch.urls")),
                path("item/", include("item.urls")),
                path("branch_location/", include("branch_location.urls")),
                path("menu/", include("menu.urls")),
                path("entity_relation/", include("entity_relation.urls")),
            ]
        ),
    ),
]
