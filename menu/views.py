from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from menu.serializer import QRMenuSerializer
from menu.services import QRMenuService


class QRMenuView(ViewSet):
    @action(detail=False, methods=["post"], url_path="create")
    def create_menu(self, request):
        qr_menu_service = QRMenuService()

        try:
            qr_menu_instance = qr_menu_service.create(request.data)

            return ResponseFactory.created(QRMenuSerializer(qr_menu_instance).data)
        except ValidationError as e:
            return ResponseFactory.bad_request(e)
        except Exception:
            return ResponseFactory.server_error()
