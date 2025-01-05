from django.apps import AppConfig


class MailTemplateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mail_template"

    def ready(self):
        from .signals import setup_email_templates

        setup_email_templates(self)
