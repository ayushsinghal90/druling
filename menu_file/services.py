import logging

from django.core.exceptions import ValidationError
from django.db import transaction

from commons.service.BaseService import BaseService
from file_upload.enum.FileType import FileType
from file_upload.services import FileUploadService
from .serializer import MenuFileCreateSerializer
from menu_file.models import MenuFile

logger = logging.getLogger(__name__)


class MenuFileService(BaseService):
    def __init__(self, file_upload_service=None):
        super().__init__(MenuFile)
        self.file_upload_service = file_upload_service or FileUploadService(
            FileType.QR_MENU
        )

    def create(self, menu, files):
        with transaction.atomic():
            try:
                file_keys = []
                for file in files:
                    file_keys.append(file.get("file_key"))
                    file["menu_id"] = menu.id

                self.file_upload_service.validate_file_exists(
                    {"branch_id": menu.branch_id}, file_keys
                )

                menu_image_serializer = MenuFileCreateSerializer(data=files, many=True)
                if menu_image_serializer.is_valid(raise_exception=True):
                    menu_image_instances = menu_image_serializer.save()

                return menu_image_instances

            except ValidationError as e:
                logger.warning(f"Validation error while saving menu files: {str(e)}")
                raise

            except Exception:
                logger.error("Error while saving menu files", exc_info=True)
                raise
