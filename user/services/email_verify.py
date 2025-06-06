from _datetime import datetime
import random

from django.conf import settings

from commons.clients.mail_client import MailClient
from commons.clients.redis_client import RedisClient
from commons.enums import RedisKey
from email_config.services import BlockedEmailService
from mail_template.config import TEMPLATE_TYPE_CONFIG
from mail_template.enum import TemplateType


class EmailVerifyService:
    def __init__(self, redis_client=None, mail_client=None, blocked_email_service=None):
        self.redis_client = redis_client or RedisClient()
        self.mail_client = mail_client or MailClient()
        self.blocked_email_service = blocked_email_service or BlockedEmailService()

    def send_code(self, data):
        email = data.get("email")

        # Check if the email is blocked
        self.blocked_email_service.verify(email)

        # Generate a 6-digit random code
        code = f"{self.get_code()}"

        # Store the code in Redis with a TTL 10 min.
        self.redis_client.set(f"{RedisKey.EMAIL_VERIFICATION}:{email}", code, 600)

        template_data = {
            "company_name": "Druling",
            "verification_code": code,
            "user_email": email,
            "support_email": "support@druling.com",
            "expiry_time": "10",
            "current_year": datetime.now().year,
        }

        # Send the code via email
        self.mail_client.send_email(
            template_name=TemplateType.EMAIL_VERIFY.value,
            template_data=template_data,
            source=TEMPLATE_TYPE_CONFIG[TemplateType.EMAIL_VERIFY.value].source,
            to_addresses=[email],
        )

    def verify(self, data):
        email = data.get("email")
        code = data.get("code")

        # Check if the email is blocked
        self.blocked_email_service.verify(email)

        stored_code = self.redis_client.get(f"{RedisKey.EMAIL_VERIFICATION}:{email}")
        if stored_code is None or stored_code != code:
            return False

        self.redis_client.set(f"{RedisKey.EMAIL_VERIFIED}:{email}", "1", 1800)
        self.redis_client.delete(f"{RedisKey.EMAIL_VERIFICATION}:{email}")
        return True

    def get_code(self):
        if settings.DEBUG:
            return "123123"
        return f"{random.randint(100000, 999999)}"
