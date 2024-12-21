from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import handle_api_exceptions
from menu.serializer import QRMenuSerializer
from menu.services import QRMenuService


class QRMenuView(ViewSet):
    def __init__(self, qr_menu_service=None, **kwargs):
        super().__init__(**kwargs)
        self.qr_menu_service = qr_menu_service or QRMenuService()

    @action(detail=False, methods=["post"], url_path="create")
    @handle_api_exceptions
    def create_menu(self, request):
        qr_menu_instance = self.qr_menu_service.create(request.data)
        return ResponseFactory.created(QRMenuSerializer(qr_menu_instance).data)
