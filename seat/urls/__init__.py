from django.urls import include, path

urlpatterns = [
    path("", include("seat.urls.seat")),
]
