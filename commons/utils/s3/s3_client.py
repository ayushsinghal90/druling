import boto3
import logging
import os
from setup import settings

logger = logging.getLogger(__name__)
localstack_port = os.getenv("LOCALSTACK_PORT", "4566")


def get_s3_client():
    """
    Get an S3 client for AWS or LocalStack.
    :return: Configured S3 client.
    """
    if settings.DEBUG:
        return boto3.client("s3", endpoint_url=f"http://localhost:{localstack_port}")
    else:
        return boto3.client("s3")


def get_s3_endpoint(bucket):
    if settings.DEBUG:
        return f"http://localhost:{localstack_port}/{bucket}"
    else:
        return f"https://{bucket}.s3.amazonaws.com"
