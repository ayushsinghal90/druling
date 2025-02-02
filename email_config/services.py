import logging

from django.db import transaction

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from .enums.blocked_type import BlockedType
from .models import BlockedEmail
from .serializer import BlockedEmailSerializer

logger = logging.getLogger(__name__)


class BlockedEmailService(BaseService):
    def __init__(self):
        super().__init__(BlockedEmail)

    def process_notification(self, body):
        logger.info(f"Processing SES notification: {body}")
        notification_type = body.get("notificationType")
        bounce_recipients = body.get("bounceRecipients")

        if notification_type == "Bounce":
            for recipient in bounce_recipients:
                self.create_or_update(
                    recipient.get("emailAddress"), BlockedType.PERMANENT
                )
        elif notification_type == "Complaint":
            for recipient in bounce_recipients:
                self.create_or_update(
                    recipient.get("emailAddress"), BlockedType.TEMPORARY
                )

    def create_or_update(self, email, blocked_type: BlockedType):
        with transaction.atomic():
            blocked_email = self.get_by_email(email)
            if blocked_email:
                blocked_email.count += 1
                blocked_email.save()
                return blocked_email

            serializer = BlockedEmailSerializer(
                data={"email": email, "type": blocked_type}
            )

            if serializer.is_valid(raise_exception=True):
                return serializer.save()

    def get_by_email(self, email):
        """
        Fetches by email.
        """
        try:
            return BlockedEmail.objects.get(email=email)
        except BlockedEmail.DoesNotExist:
            return None
        except Exception as e:
            logger.error(f"Error fetching contact: {str(e)}", exc_info=True)
            raise BaseError("Error while fetching branch contact", original_exception=e)
