from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
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

    @api_handler()
    @permission_classes([AllowAny])
    def get_menu_by_id(self, request, menu_id):
        qr_menu_obj = self.qr_menu_service.get_by_id(menu_id)
        return ResponseFactory.success(QRMenuGetSerializer(qr_menu_obj).data)

    @api_handler()
    def get_menu_by_branch_id(self, request, branch_id):
        qr_menu_obj = self.qr_menu_service.get_by_branch_id(branch_id)
        return ResponseFactory.success(QRMenuGetSerializer(qr_menu_obj).data)

    @api_handler()
    def get_all(self, request):
        profile_id = request.user.profile.id
        qr_menu_objs = self.qr_menu_service.get_list(profile_id)
        return ResponseFactory.success(
            QRMenuGetSerializer(qr_menu_objs, many=True).data
        )


class QRMenuPublicView(ViewSet):
    permission_classes = [AllowAny]  # Set permission at class level

    def __init__(self, qr_menu_service=None, **kwargs):
        super().__init__(**kwargs)
        self.qr_menu_service = qr_menu_service or QRMenuService()

    @api_handler()
    def get_menu_by_id(self, request, menu_id):
        qr_menu_obj = self.qr_menu_service.get_by_id(menu_id)
        return ResponseFactory.success(QRMenuGetSerializer(qr_menu_obj).data)
