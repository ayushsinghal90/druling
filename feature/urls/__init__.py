from django.urls import include, path

urlpatterns = [
    path("profile/", include("feature.urls.profile_feature")),
]
