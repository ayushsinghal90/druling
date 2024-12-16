import logging

from django.db import transaction
from rest_framework.exceptions import ValidationError

from branch.services import BranchService
from commons.service.BaseService import BaseService
from menu.models import QRMenu
from menu.serializer import QRMenuSerializer

logger = logging.getLogger(__name__)


class QRMenuService(BaseService):
    def __init__(self, branch_service=None):
        super().__init__(QRMenu)
        self.branch_service = branch_service or BranchService()

    def create(self, menu_data):
        try:
            branch_id = menu_data.get("branch_id")
            self.branch_service.get_by_id(branch_id)

            qr_menu_serializer = QRMenuSerializer(data=menu_data)
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
