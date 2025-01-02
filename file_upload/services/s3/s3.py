import boto3
import logging
import os
from setup import settings

logger = logging.getLogger(__name__)
localstack_port = os.getenv("LOCALSTACK_PORT", "4566")


class S3Service:
    @staticmethod
    def get_client():
        """
        Get an S3 client for AWS or LocalStack.
        :return: Configured S3 client.
        """
        if settings.DEBUG:
            return boto3.client(
                "services", endpoint_url=f"http://localhost:{localstack_port}"
            )
        else:
            return boto3.client("services")

    @staticmethod
    def get_endpoint(bucket):
        if settings.DEBUG:
            return f"http://localhost:{localstack_port}/{bucket}"
        else:
            return f"https://{bucket}.services.amazonaws.com"
