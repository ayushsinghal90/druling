import logging
from typing import Optional, List, Dict, Any
from botocore.exceptions import ClientError
from commons.exceptions.BaseError import BaseError
from file_upload.services.s3 import S3Service

logger = logging.getLogger(__name__)


class S3ReadService:
    def __init__(
        self,
        bucket_name: str,
        object_key: Optional[str] = None,
        object_keys: Optional[List[str]] = None,
    ):
        """
        Initialize S3ReadService.

        Args:
            bucket_name: Name of the S3 bucket
            object_key: Single object key to operate on
            object_keys: List of object keys to operate on
        """
        self.s3_client = S3Service.get_client()
        self.bucket_name = bucket_name
        self.object_key = object_key
        self.object_keys = object_keys

    def _validate_object_key(self) -> str:
        """Validate and return object key."""
        if not self.object_key:
            raise ValueError("object_key must be provided")
        return self.object_key

    def _validate_object_keys(self) -> List[str]:
        """Validate and return object keys."""
        if not self.object_keys:
            raise ValueError("object_keys must be provided")
        return self.object_keys

    def _handle_s3_error(self, operation: str, error: Exception) -> None:
        """Handle S3 operation errors consistently."""
        logger.error(f"Error during {operation}: {error}")
        raise BaseError(f"Error during {operation}", original_exception=error)

    def get_read_signed_url(self, expires_in: int = 3600) -> str:
        """
        Generate a pre-signed URL for reading an object.

        Args:
            expires_in: URL expiration time in seconds

        Returns:
            Pre-signed URL string
        """
        try:
            params: Dict[str, Any] = {
                "Bucket": self.bucket_name,
                "Key": self._validate_object_key(),
            }
            return self.s3_client.generate_presigned_url(
                "get_object", Params=params, ExpiresIn=expires_in
            )
        except Exception as e:
            self._handle_s3_error("generating signed URL", e)

    def get_normal_url(self) -> str:
        """Generate a normal URL for an S3 object."""
        return (
            f"{S3Service.get_endpoint(self.bucket_name)}/{self._validate_object_key()}"
        )

    def get_file(self) -> bytes:
        """Get file content as bytes."""
        try:
            response = self.s3_client.get_object(
                Bucket=self.bucket_name, Key=self._validate_object_key()
            )
            return response["Body"].read()
        except Exception as e:
            self._handle_s3_error("fetching file", e)

    def list_objects(self, prefix: str = "") -> List[str]:
        """
        List objects in bucket with prefix.

        Args:
            prefix: Filter objects by prefix

        Returns:
            List of object keys
        """
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name, Prefix=prefix
            )
            return [obj["Key"] for obj in response.get("Contents", [])]
        except Exception as e:
            self._handle_s3_error("listing objects", e)

    def file_exists(self) -> bool:
        """Check if file exists in bucket."""
        try:
            self.s3_client.head_object(
                Bucket=self.bucket_name, Key=self._validate_object_key()
            )
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return False
            self._handle_s3_error("checking file existence", e)

    def files_exist(self, folder_prefix: str) -> bool:
        """
        Check if multiple files exist in bucket folder.

        Args:
            folder_prefix: Folder path in bucket

        Returns:
            True if all files exist
        """
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name, Prefix=folder_prefix
            )
            existing_keys = {obj["Key"] for obj in response.get("Contents", [])}
            return all(
                f"{folder_prefix}/{key}" in existing_keys
                for key in self._validate_object_keys()
            )
        except Exception as e:
            self._handle_s3_error("checking files existence", e)
