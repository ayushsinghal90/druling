import json

from botocore.exceptions import ClientError
from typing import List, Dict, Any

from commons.clients.boto_client import boto_client
from commons.exceptions.BaseError import BaseError


class MailClient:
    def __init__(self):
        self.client = boto_client("ses")

    def get_client(self):
        return self.client

    def send_email(
        self,
        source: str,
        to_addresses: List[str],
        template_name: str,
        template_data,
    ) -> Dict[str, Any]:
        """
        Send templated email using SES.

        Args:
            source (str): Sender email address
            to_addresses (List[str]): List of recipient email addresses
            template_name (str): Name of the SES template to use
            template_data (Dict[str, Any]): Template data

        Returns:
            Dict[str, Any]: Response from SES
        """
        try:
            response = self.client.send_templated_email(
                Source=source,
                Destination={"ToAddresses": to_addresses},
                Template=template_name,
                TemplateData=json.dumps(template_data),
            )
            return response
        except ClientError as e:
            raise BaseError(f"Failed to send templated email: {str(e)}")
