import logging
from typing import Dict, Any

from mail_template.config import TEMPLATE_TYPE_CONFIG
from mail_template.enum import TemplateType
from mail_template.template_manager import TemplateManager

logger = logging.getLogger(__name__)


class TemplateSetup:
    def __init__(self, template_manager=None):
        self.template_manager = template_manager or TemplateManager()

    def setup_templates(self, force_update: bool = False) -> Dict[str, Any]:
        """
        Set up all email templates in SES and return status of each template.
        """
        results = self.starting_templates_setup(force_update)
        errors, success = [], []
        errors, success = [k for k, v in results.items() if v["status"] == "error"], [
            k for k, v in results.items() if v["status"] != "error"
        ]
        logger.info(
            f"Ran script to set up email templates. Success: {success}, Errors: {errors}"
        )

    def starting_templates_setup(self, force_update: bool = False) -> Dict[str, Any]:
        """
        Set up all email templates in SES and return status of each template.
        """
        results = {}

        for template_type in TemplateType:
            template_config = TEMPLATE_TYPE_CONFIG[template_type.value]
            try:
                action, result = self.template_manager.create_or_update_template(
                    template_name=template_config.template_name,
                    subject=template_config.subject,
                    html_content=template_config.html,
                    text_content=template_config.text,
                    force_update=force_update,
                )
                results[template_type.value] = {
                    "status": "success",
                    "action": action,
                    "response": result,
                }
                logger.info(f"Successfully {action} template: {template_type.value}")
            except Exception as e:
                results[template_type.value] = {"status": "error", "error": str(e)}
                logger.error(
                    f"Failed to set up template {template_type.value}: {str(e)}"
                )

        return results
