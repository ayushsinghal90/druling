from .service import TemplateSetup
import logging

logger = logging.getLogger(__name__)


def setup_email_templates(sender, **kwargs):
    """
    Signal handler to set up email templates after migrations
    """
    try:
        TemplateSetup().setup_templates()
        logger.info("Successfully set up email templates")
    except Exception as e:
        logger.error(f"Failed to set up email templates: {str(e)}")
