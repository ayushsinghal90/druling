import boto3

from django.conf import settings


def boto_client(service=None, config=None):
    if service is None:
        raise ValueError("Service name is required")

    if settings.DEBUG:
        return boto3.client(
            service,
            endpoint_url=f"http://{settings.LOCALSTACK_HOST}:{settings.LOCALSTACK_PORT}",
            region_name=settings.AWS_DEFAULT_REGION,
        )
    else:
        # Production AWS configuration
        return boto3.client(
            service, region_name=settings.AWS_DEFAULT_REGION, config=config
        )
