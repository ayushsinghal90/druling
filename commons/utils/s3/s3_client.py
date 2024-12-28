import boto3
import logging
from setup import settings

logger = logging.getLogger(__name__)


def get_s3_client():
    """
    Get an S3 client for AWS or LocalStack.
    :return: Configured S3 client.
    """
    if settings.DEBUG:
        return boto3.client("s3", endpoint_url="http://localhost:4566")
    else:
        return boto3.client("s3")
