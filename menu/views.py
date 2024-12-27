from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from menu.serializer import UploadMenuSerializer, QRMenuSerializer
from commons.middleware.api_handler import api_handler
from menu.services import QRMenuService
from menu.utils import copy_file_if_exists


class QRMenuView(ViewSet):
    def __init__(self, qr_menu_service=None, **kwargs):
        super().__init__(**kwargs)
        self.qr_menu_service = qr_menu_service or QRMenuService()

    @api_handler(serializer=UploadMenuSerializer)
    def create_menu(self, request):
        new_file_location = copy_file_if_exists(request.data.get("file_key"))
        qr_menu_obj = self.qr_menu_service.create(
            branch_id=request.data.get("branch_id"), file_key=new_file_location
        )
        return ResponseFactory.created(QRMenuSerializer(qr_menu_obj).data)
