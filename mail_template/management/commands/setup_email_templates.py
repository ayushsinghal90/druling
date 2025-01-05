from django.core.management.base import BaseCommand
from ...service import TemplateSetup
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Sets up or updates all SES email templates"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force update all templates even if they exist",
        )

    def handle(self, *args, **options):
        try:
            force_update = options.get("force", False)

            TemplateSetup().setup_templates(force_update)
            self.stdout.write(self.style.SUCCESS("Successfully set up email templates"))
        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f"Failed to set up email templates: {str(e)}")
            )
