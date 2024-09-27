from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth", views.obtain_auth_token),
    path(
        "api/",
        include(
            [
                path("", include("user.urls")),
                path("restaurant/", include("restaurant.urls")),
                path("branch/", include("branch.urls")),
                path("item/", include("item.urls")),
                path("branch_location/", include("branch_location.urls")),
                path("qr_menu/", include("menu.urls")),
            ]
        ),
    ),
]
