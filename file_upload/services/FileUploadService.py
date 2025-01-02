import uuid

from django.core.exceptions import ValidationError

from file_upload.config import S3_FILE_TYPE_CONFIG
from file_upload.enum.FileType import FileType
from file_upload.services.s3 import S3ReadService, S3UploadService


class FileUploadService:
    def __init__(
        self,
        file_type: FileType,
    ):
        self.file_type = file_type
        self.bucket = S3_FILE_TYPE_CONFIG[file_type].bucket

    def get_upload_url_and_file_key(self, file_key, path_params=None):
        new_file_key = f"{uuid.uuid4()}-{file_key}"
        new_file_path = f"{self.get_sub_path(path_params)}/{new_file_key}"
        signed_url = S3UploadService(self.bucket, new_file_path).get_upload_signed_url()
        return {
            "upload_url": signed_url,
            "new_file_key": new_file_key,
            "file_key": file_key,
        }

    def get_sub_path(self, path_params=None):
        return S3_FILE_TYPE_CONFIG[self.file_type].path(path_params)

    def get_url(self, file_key, path_params=None):
        return S3ReadService(
            self.bucket, f"{self.get_sub_path(path_params)}/{file_key}"
        ).get_normal_url()

    def get_menu_upload_url(self, path_params, files):
        result = []
        for file in files:
            result.append(
                self.get_upload_url_and_file_key(
                    file.get("file_key"), path_params=path_params
                )
            )
        return result

    def get_s3_read_service(self, path_params=None, file_key=None, file_keys=None):
        if not file_key and not file_keys:
            raise ValueError("file_key or file_keys must be provided")

        if file_key:
            object_key = f"{self.get_sub_path(path_params)}/{file_key}"
            return S3ReadService(self.bucket, object_key)
        return S3ReadService(self.bucket, object_keys=file_keys)

    def validate_file_exists(self, path_params, file_keys):
        s3_read_service = self.get_s3_read_service(
            path_params=path_params, file_keys=file_keys
        )
        if not (s3_read_service.files_exist(self.get_sub_path(path_params))):
            raise ValidationError("One or more File not found")
