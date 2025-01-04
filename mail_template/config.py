from mail_template.enum import TemplateType
from .data_model import TemplateConfig
from .templates import EMAIL_VERIFY


TEMPLATE_TYPE_CONFIG = {
    TemplateType.EMAIL_VERIFY.value: TemplateConfig(
        template_name=TemplateType.EMAIL_VERIFY.value,
        subject="Verify your email",
        html=EMAIL_VERIFY.html_part,
        text=EMAIL_VERIFY.text_part,
    )
}
