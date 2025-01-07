import logging

from commons.clients.boto_client import boto_client
from setup import settings

logger = logging.getLogger(__name__)


class S3Service:
    @staticmethod
    def get_client():
        """
        Get an S3 client for AWS or LocalStack.
        :return: Configured S3 client.
        """
        return boto_client("s3")

    @staticmethod
    def get_endpoint(bucket):
        if settings.DEBUG:
            return f"http://localhost:{settings.LOCALSTACK_PORT}/{bucket}"
        else:
            return f"https://{bucket}.s3.amazonaws.com"
