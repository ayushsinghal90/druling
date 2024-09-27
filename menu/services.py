import logging

from django.db import transaction
from rest_framework.exceptions import ValidationError

from menu.serializer import QRMenuSerializer

logger = logging.getLogger(__name__)


class QRMenuService:
    def create(self, request):
        try:
            data = {
                "branch_id": request.data.get("branch_id"),
                "file_key": request.data.get("file_key"),
            }

            qr_menu_serializer = QRMenuSerializer(data=data)

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
