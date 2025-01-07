from .service import TemplateSetup
import logging

logger = logging.getLogger(__name__)


def setup_email_templates(sender, **kwargs):
    """
    Signal handler to set up email templates after migrations
    """
    logger.info("Running script to Set up email templates")
    TemplateSetup().setup_templates()
    logger.info("Completing script to set up email templates")
