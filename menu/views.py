from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from menu.requests import CreateQRMenuSerializer
from menu.serializer import QRMenuGetSerializer
from commons.middleware.api_handler import api_handler
from menu.services import QRMenuService
from menu_file.services import MenuFileService


class QRMenuView(ViewSet):
    def __init__(self, qr_menu_service=None, menu_file_service=None, **kwargs):
        super().__init__(**kwargs)
        self.qr_menu_service = qr_menu_service or QRMenuService()
        self.menu_file_service = menu_file_service or MenuFileService()

    @api_handler(serializer=CreateQRMenuSerializer)
    def create_menu(self, request):
        qr_menu_obj = self.qr_menu_service.create(request.data)
        return ResponseFactory.created(QRMenuGetSerializer(qr_menu_obj).data)

    @api_handler(serializer=CreateQRMenuSerializer)
    def get_menu_upload_url(self, request):
        upload_creds = self.menu_file_service.get_menu_upload_url(request.data)
        return ResponseFactory.created(upload_creds)

    @api_handler()
    def get_menu_details(self, request, menu_id):
        qr_menu_obj = self.qr_menu_service.get_by_id(menu_id)
        return ResponseFactory.success(QRMenuGetSerializer(qr_menu_obj).data)
