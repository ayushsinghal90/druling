from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from menu.requests import CreateQRMenuSerializer, MenuFileNameSerializer
from menu.serializer import QRMenuSerializer
from commons.middleware.api_handler import api_handler
from menu.services import QRMenuService


class QRMenuView(ViewSet):
    def __init__(self, qr_menu_service=None, **kwargs):
        super().__init__(**kwargs)
        self.qr_menu_service = qr_menu_service or QRMenuService()

    @api_handler(serializer=CreateQRMenuSerializer)
    def create_menu(self, request):
        qr_menu_obj = self.qr_menu_service.create(
            branch_id=request.data.get("branch_id"),
            file_key=request.data.get("file_key"),
        )
        return ResponseFactory.created(QRMenuSerializer(qr_menu_obj).data)

    @api_handler(serializer=MenuFileNameSerializer)
    def get_menu_upload_url(self, request):
        upload_creds = self.qr_menu_service.get_menu_upload_url(
            request.data.get("file_key")
        )
        return ResponseFactory.created(upload_creds)
