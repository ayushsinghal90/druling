from typing import Dict, Any, Tuple
from botocore.exceptions import ClientError
import logging

from commons.clients.mail_client import MailClient

logger = logging.getLogger(__name__)


class TemplateManager:
    def __init__(self, client=None):
        self.client = client or MailClient()

    def create_or_update_template(
        self,
        template_name: str,
        subject: str,
        html_content: str,
        text_content: str,
        force_update: bool = False,
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Create a new template or update if it exists.

        Args:
            template_name: Name of the template
            subject: Subject line template
            html_content: HTML version of the template
            text_content: Plain text version of the template
            force_update: Whether to force update existing template

        Returns:
            Tuple containing action taken ('created' or 'updated') and response
        """
        template_data = {
            "TemplateName": template_name,
            "SubjectPart": subject,
            "HtmlPart": html_content,
            "TextPart": text_content,
        }

        try:
            # Check if template exists
            if force_update:
                return self._update_template(template_data)

            try:
                self.client.get_template(TemplateName=template_name)
                return self._update_template(template_data)
            except ClientError as e:
                if e.response["Error"]["Code"] == "TemplateDoesNotExist":
                    return self._create_template(template_data)
                raise

        except ClientError as e:
            logger.error(f"Failed to manage template {template_name}: {str(e)}")
            raise

    def _create_template(
        self, template_data: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """Create a new template."""
        response = self.client.create_template(Template=template_data)
        logger.info(f"Created template: {template_data['TemplateName']}")
        return "created", response

    def _update_template(
        self, template_data: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """Update an existing template."""
        response = self.client.update_template(Template=template_data)
        logger.info(f"Updated template: {template_data['TemplateName']}")
        return "updated", response

    def delete_template(self, template_name: str) -> Dict[str, Any]:
        """Delete a template."""
        return self.client.delete_template(TemplateName=template_name)

    def get_template(self, template_name: str) -> Dict[str, Any]:
        """Get template details."""
        return self.client.get_template(TemplateName=template_name)

    def list_templates(self) -> Dict[str, Any]:
        """List all templates."""
        return self.client.list_templates()
