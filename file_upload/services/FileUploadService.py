import uuid

from file_upload.services.BasePathSerivce import BasePathService
from file_upload.enum.Buckets import BucketType
from file_upload.enum.FIleType import FileType
from file_upload.services.s3 import S3ReadService, S3UploadService


class FileUploadService:
    def __init__(
        self,
        bucket: BucketType,
        file_type: FileType,
    ):
        self.file_type = file_type
        self.bucket = bucket
        self.base_path_service = BasePathService()

    def get_upload_url_and_file_key(self, file_key, path_params=None):
        new_file_key = f"{uuid.uuid4()}-{file_key}"
        new_file_path = f"{self.get_sub_path(path_params)}/{new_file_key}"
        signed_url = S3UploadService(
            self.bucket.value, new_file_path
        ).get_upload_signed_url()
        return {
            "upload_url": signed_url,
            "new_file_key": new_file_key,
            "file_key": file_key,
        }

    def get_sub_path(self, path_params=None):
        return self.base_path_service.get_sub_path(self.file_type, params=path_params)

    def get_url(self, file_key, path_params=None):
        return S3ReadService(
            self.bucket.value, f"{self.get_sub_path(path_params)}/{file_key}"
        ).get_normal_url()

    def get_s3_read_service(self, path_params=None, file_key=None, file_keys=None):
        if not file_key and not file_keys:
            raise ValueError("file_key or file_keys must be provided")

        if file_key:
            object_key = f"{self.get_sub_path(path_params)}/{file_key}"
            return S3ReadService(self.bucket.value, object_key)
        return S3ReadService(self.bucket.value, object_keys=file_keys)
