from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MailTemplateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mail_template"

    def ready(self):
        from .signals import setup_email_templates

        post_migrate.connect(setup_email_templates, sender=self)
