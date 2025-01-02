import logging
from commons.exceptions.BaseError import BaseError
from file_upload.services.s3 import S3Service

logger = logging.getLogger(__name__)


class S3UploadService:
    def __init__(self, bucket_name: str, object_key: str):
        """Initialize S3UploadService."""
        self.s3_client = S3Service.get_client()
        self.bucket_name = bucket_name
        self.object_key = object_key

    def _handle_s3_error(self, operation: str, error: Exception) -> None:
        """Handle S3 operation errors consistently."""
        logger.error(f"Error during {operation}: {error}")
        raise BaseError(f"Error while {operation}", original_exception=error)

    def get_upload_signed_url(self, expires_in: int = 3600) -> str:
        """
        Generate a pre-signed URL for uploading.

        Args:
            expires_in: URL expiration time in seconds

        Returns:
            Pre-signed URL string
        """
        try:
            return self.s3_client.generate_presigned_url(
                "put_object",
                Params={"Bucket": self.bucket_name, "Key": self.object_key},
                ExpiresIn=expires_in,
            )
        except Exception as e:
            self._handle_s3_error("generating upload URL", e)

    def upload_file(self, file_path: str) -> None:
        """
        Upload file to S3.

        Args:
            file_path: Path to local file
        """
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, self.object_key)
            logger.info(
                f"File {file_path} uploaded to {self.bucket_name}/{self.object_key}"
            )
        except Exception as e:
            self._handle_s3_error("uploading file", e)
