from django.urls import include, path

urlpatterns = [
    path("", include("item.urls.item")),
]
