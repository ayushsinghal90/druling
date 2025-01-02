import logging

from django.core.exceptions import ValidationError
from django.db import transaction

from commons.service.BaseService import BaseService
from file_upload.enum.Buckets import BucketType
from file_upload.enum.FIleType import FileType
from file_upload.services import FileUploadService
from .serializer import MenuFileCreateSerializer
from menu_file.models import MenuFile

logger = logging.getLogger(__name__)


class MenuFileService(BaseService):
    def __init__(self, file_upload_service=None):
        super().__init__(MenuFile)
        self.file_upload_service = file_upload_service or FileUploadService(
            BucketType.MENU, FileType.QR_MENU
        )

    def create(self, menu, files):
        with transaction.atomic():
            try:
                file_keys = []
                for file in files:
                    file_keys.append(file.get("file_key"))
                    file["menu_id"] = menu.id

                self.validate_file_exists(menu.branch_id, file_keys)

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
        path_params = {"branch_id": branch_id}
        s3_read_service = self.file_upload_service.get_s3_read_service(
            path_params=path_params, file_keys=file_keys
        )
        if not (
            s3_read_service.files_exist(
                self.file_upload_service.get_sub_path(path_params)
            )
        ):
            logger.error("One or more File not found", exc_info=True)
            raise ValidationError("One or more File not found")

    def get_menu_upload_url(self, data):
        branch_id = data.get("branch_id")
        files = data.get("files")

        result = []
        for file in files:
            result.append(
                self.file_upload_service.get_upload_url_and_file_key(
                    file.get("file_key"), path_params={"branch_id": branch_id}
                )
            )
        return result
