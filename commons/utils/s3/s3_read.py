from commons.exceptions.BaseError import BaseError
from .s3_client import get_s3_client
import logging


logger = logging.getLogger(__name__)
s3_client = get_s3_client()


def get_read_signed_url(bucket_name, object_key, expires_in=3600):
    """
    Generate a pre-signed URL for reading/viewing/downloading an object.
    :param bucket_name: Name of the bucket.
    :param object_key: Key of the object.
    :param expires_in: Expiration time in seconds.
    :return: Pre-signed URL.
    """
    try:
        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=expires_in,
        )
        return url
    except Exception as e:
        logger.error(f"Error generating read signed URL: {e}")
        raise BaseError("Error while retrieving file.", original_exception=e)


def get_normal_url(bucket_name, object_key):
    """
    Generate a normal URL for an S3 object.
    :param bucket_name: Name of the bucket.
    :param object_key: Key of the object.
    :return: Normal URL.
    """
    return f"https://{bucket_name}.s3.amazonaws.com/{object_key}"


def get_file(bucket_name, object_key):
    """
    Get the content of an object without using a signed URL.
    :param bucket_name: Name of the bucket.
    :param object_key: Key of the object.
    :return: File content as bytes.
    """
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        return response["Body"].read()
    except Exception as e:
        logger.error(f"Error fetching file: {e}")
        raise BaseError("Error while retrieving file.", original_exception=e)


def list_objects(bucket_name, prefix=""):
    """
    List objects in a bucket with a specific prefix.
    :param bucket_name: Name of the bucket.
    :param prefix: Prefix for filtering objects.
    :return: List of object keys.
    """
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        if "Contents" in response:
            return [obj["Key"] for obj in response["Contents"]]
        return []
    except Exception as e:
        logger.error(f"Error listing objects: {e}")
        raise BaseError("Error while retrieving files.", original_exception=e)


def file_exists(bucket_name, object_key):
    """
    Check if a file exists in the S3 bucket.
    :param bucket_name: Name of the bucket.
    :param object_key: Key of the object.
    :return: True if the file exists, False otherwise.
    """
    try:
        s3_client.head_object(Bucket=bucket_name, Key=object_key)
        return True
    except s3_client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            return False
        else:
            logger.error(f"Error checking if file exists: {e}")
            raise BaseError(
                "Error while checking file existence.", original_exception=e
            )


def files_exist(bucket_name, folder_prefix, object_keys):
    """
    Check if multiple files exist in the S3 bucket folder.
    :param bucket_name: Name of the bucket.
    :param folder_prefix: Prefix (folder path) in the bucket.
    :param object_keys: List of object keys to check.
    :return: True if all files exist, False otherwise.
    """
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)
        existing_keys = {obj["Key"] for obj in response.get("Contents", [])}
        return all(f"{folder_prefix}/{key}" in existing_keys for key in object_keys)
    except Exception as e:
        logger.error(f"Error listing objects: {e}")
        raise BaseError("Error while checking file existence.", original_exception=e)
