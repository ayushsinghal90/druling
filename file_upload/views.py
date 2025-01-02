from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from file_upload.enum.FileType import FileType
from file_upload.requests.serializers import FileUploadSerializer
from file_upload.services import FileUploadService
from commons.middleware.api_handler import api_handler


class FileUploadView(ViewSet):
    @api_handler(serializer=FileUploadSerializer)
    def get_upload_url(self, request):
        file_upload_service = FileUploadService(FileType(request.data.get("file_type")))
        path_params = request.data.get("params")
        files = request.data.get("files")

        upload_urls = file_upload_service.get_menu_upload_url(path_params, files)
        return ResponseFactory.created(upload_urls)
