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
                path("user/", include("user.urls")),
                path("restaurant/", include("restaurant.urls")),
                path("branch/", include("branch.urls")),
                path("item/", include("item.urls")),
                path("branch-location/", include("branch_location.urls")),
                path("menu/", include("menu.urls")),
                path("menu-file/", include("menu_file.urls")),
                path("entity-relation/", include("entity_relation.urls")),
            ]
        ),
    ),
]
