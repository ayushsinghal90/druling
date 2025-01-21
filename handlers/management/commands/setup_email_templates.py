from django.core.management.base import BaseCommand
from mail_template.service import TemplateSetup
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
        self.stdout.write(
            self.style.SUCCESS("Running script to Set up email templates")
        )
        force_update = options.get("force", False)
        TemplateSetup().setup_templates(force_update)
        self.stdout.write(
            self.style.SUCCESS("Completing script to set up email templates")
        )
