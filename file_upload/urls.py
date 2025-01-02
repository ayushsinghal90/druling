from django.urls import path
from .views import FileUploadView

urlpatterns = [
    path("upload_url/", FileUploadView.as_view({"post": "get_menu_upload_url"})),
]
