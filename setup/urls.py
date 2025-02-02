from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

from setup.views import CustomTokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("auth/", include("social_django.urls", namespace="social")),
    path("health/", include("health_check.urls")),
    path(
        "api/",
        include(
            [
                path("user/", include("user.urls")),
                path("profile/", include("profile.urls")),
                path("restaurant/", include("restaurant.urls")),
                path("branch/", include("branch.urls")),
                path("item/", include("item.urls")),
                path("branch_location/", include("branch_location.urls")),
                path("menu/", include("menu.urls")),
                path("menu-file/", include("menu_file.urls")),
                path("entity-relation/", include("entity_relation.urls")),
                path("file/", include("file_upload.urls")),
                path("subscription_plan/", include("subscription_plan.urls")),
                path("transaction/", include("transaction.urls")),
                path("subscription/", include("subscription.urls")),
                path("email/", include("email.urls")),
            ]
        ),
    ),
]
