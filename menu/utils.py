import uuid
import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from setup import settings

logger = logging.getLogger(__name__)


def get_boto_params():
    params = {}
    if settings.DEBUG:
        params['aws_access_key_id'] = 'test'
        params['aws_secret_access_key'] = 'test'
        params['endpoint_url'] = 'http://localhost:4566'
        params['region_name'] = 'ap-south-1'
    return params


def copy_file_if_exists(file_key, source_bucket='druling-menus-temp',
                        destination_bucket='druling-menus'):
    """
    Checks if a file exists in the source S3 bucket and copies it to the destination bucket if found.

    :param source_bucket: Name of the source S3 bucket.
    :param destination_bucket: Name of the destination S3 bucket.
    :param file_key: Key of the file in the source bucket to check and copy.
    :return: True if the file was copied successfully, False otherwise.
    """
    destination_key = f"{uuid.uuid4()}-{file_key}"
    s3_client = boto3.client('s3', **get_boto_params())

    try:
        # Check if the file exists in the source bucket
        s3_client.head_object(Bucket=source_bucket, Key=file_key)
        logger.info(f"File '{file_key}' found in bucket '{source_bucket}'.")

        # Copy the file to the destination bucket
        copy_source = {'Bucket': source_bucket, 'Key': file_key}
        s3_client.copy(copy_source, destination_bucket, destination_key)
        logger.info(f"File '{file_key}' successfully copied to bucket '{destination_bucket}' with key '{destination_key}'.")
        return destination_key
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            logger.error(f"File '{file_key}' not found in bucket '{source_bucket}'.")
        else:
            logger.error(f"An error occurred: {e}")
    except (NoCredentialsError, PartialCredentialsError):
        logger.error("AWS credentials not found or incomplete.")
    return False
