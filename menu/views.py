from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny

from commons.api.responses import ResponseFactory
from menu.serializer import UploadMenuSerializer
from commons.middleware.api_handler import api_handler
from menu.requests.qr_menu_create_serializer import CreateQRMenuSerializer
from menu.services import QRMenuService
from menu.utils import copy_file_if_exists


class QRMenuView(ViewSet):

    # TODO: remove this
    permission_classes = (AllowAny,)

    def __init__(self, qr_menu_service=None, **kwargs):
        super().__init__(**kwargs)
        self.qr_menu_service = qr_menu_service or QRMenuService()

    @action(detail=False, methods=["post"], url_path="create")
    @api_handler(serializer=CreateQRMenuSerializer)
    def create_menu(self, request):
        upload_menu_serializer = UploadMenuSerializer(data=request.data)
        if not upload_menu_serializer.is_valid():
            return ResponseFactory.bad_request(errors=upload_menu_serializer.errors)

        new_file_location = copy_file_if_exists(request.data.get('file_key'))

        try:
            self.qr_menu_service.create(branch_id=request.data.get('branch_id'),
                                        file_key=new_file_location)
            return ResponseFactory.created(
                message="Menu Uploaded Successfully",
            )
        except ValidationError as e:
            return ResponseFactory.bad_request(e)
        except Exception as e:
            return ResponseFactory.server_error(e)
