from django.urls import include, path

urlpatterns = [
    path("", include("order.urls.order")),
]
