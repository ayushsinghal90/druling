import logging

from django.core.exceptions import ValidationError
from django.db import transaction

from branch.services import BranchService
from commons.service.BaseService import BaseService
from commons.utils.s3.s3_read import file_exists
from menu.models import QRMenu
from menu.serializer import QRMenuSerializer
from menu.utils import get_upload_url_and_file_key, get_menu_path

logger = logging.getLogger(__name__)
MENU_BUCKET = "druling-menus"
QR_MENU_FOLDER = "qr_menus"


class QRMenuService(BaseService):
    def __init__(self, branch_service=None):
        super().__init__(QRMenu)
        self.branch_service = branch_service or BranchService()

    def create(self, branch_id, file_key):
        try:
            file_path = get_menu_path(QR_MENU_FOLDER, file_key)
            if not file_exists(MENU_BUCKET, file_path):
                raise ValidationError("File not found.")
            qr_menu_serializer = QRMenuSerializer(
                data={"branch_id": branch_id, "file_key": file_key}
            )
            if qr_menu_serializer.is_valid(raise_exception=True):
                with transaction.atomic():
                    qr_menu_instance = qr_menu_serializer.save()

                return qr_menu_instance

        except ValidationError as e:
            logger.warning(f"Validation error while creating QR menu: {str(e)}")
            raise

        except Exception:
            logger.error("Error while creating QR menu", exc_info=True)
            raise

    def get_menu_upload_url(self, key_name):
        return get_upload_url_and_file_key(MENU_BUCKET, QR_MENU_FOLDER, key_name)
