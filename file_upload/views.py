from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from file_upload.requests.serializers import FileUploadSerializer
from file_upload.services import FileUploadService
from commons.middleware.api_handler import api_handler


class QRMenuView(ViewSet):
    @api_handler(serializer=FileUploadSerializer)
    def get_menu_upload_url(self, request):
        file_upload_service = FileUploadService(request.data.get("file_type"))
        upload_urls = file_upload_service.get_menu_upload_url(request.data)
        return ResponseFactory.created(upload_urls)
