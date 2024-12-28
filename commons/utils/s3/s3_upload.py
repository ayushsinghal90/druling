from commons.exceptions.BaseError import BaseError
from .s3_client import get_s3_client
import logging


logger = logging.getLogger(__name__)
s3_client = get_s3_client()


def get_upload_signed_url(bucket_name, object_key, expires_in=3600):
    """
    Generate a pre-signed URL for uploading an object.
    :param bucket_name: Name of the bucket.
    :param object_key: Key of the object.
    :param expires_in: Expiration time in seconds.
    :return: Pre-signed URL.
    """
    try:
        url = s3_client.generate_presigned_url(
            "put_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=expires_in,
        )
        return url
    except Exception as e:
        logger.error(f"Error generating upload signed URL: {e}")
        raise BaseError("Error while uploading file.", original_exception=e)


def upload_file(bucket_name, object_key, file_path):
    """
    Upload a file to S3.
    :param bucket_name: Name of the bucket.
    :param object_key: Key of the object in S3.
    :param file_path: Path to the local file to upload.
    :return: None
    """
    try:
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"File {file_path} uploaded to {bucket_name}/{object_key}")
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        raise BaseError("Error while uploading file.", original_exception=e)
