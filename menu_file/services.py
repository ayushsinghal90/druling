import logging

from django.core.exceptions import ValidationError
from django.db import transaction

from commons.service.BaseService import BaseService
from commons.utils.s3.s3_read import files_exist
from .serializer import MenuFileCreateSerializer
from .utils import get_upload_url_and_file_key, MENU_BUCKET, get_sub_path
from menu_file.models import MenuFile

logger = logging.getLogger(__name__)


class MenuFileService(BaseService):
    def __init__(self):
        super().__init__(MenuFile)

    def create(self, menu, files):
        with transaction.atomic():
            try:
                file_keys = []
                for file in files:
                    file_keys.append(file.file_key)
                    file["menu_id"] = menu.id

                self.validate_file_exists(menu.branch_id, files)

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

    def validate_file_exists(self, branch_id, file_keys):
        if not files_exist(MENU_BUCKET, get_sub_path(branch_id), file_keys):
            logger.error("One or more File not found", exc_info=True)
            raise ValidationError("One or more File not found")

    def get_menu_upload_url(self, data):
        branch_id = data.get("branch_id")
        files = data.get("files")

        result = []
        for file in files:
            result.append(get_upload_url_and_file_key(branch_id, file.file_key))
        return result
