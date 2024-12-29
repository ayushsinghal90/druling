import logging

from django.core.exceptions import ValidationError
from django.db import transaction

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from contact.models import Contact
from .models import SocialContact
from .serializer import SocialContactCreateSerializer

logger = logging.getLogger(__name__)


class SocialContactService(BaseService):
    def __init__(self):
        super().__init__(SocialContact)

    def create(self, contact: Contact, data):
        with transaction.atomic():
            try:
                if not contact or not contact.id:
                    raise ValidationError("Contact does not exist")
                data["contact_id"] = contact.id

                social_contact_serializer = SocialContactCreateSerializer(data=data)
                if social_contact_serializer.is_valid(raise_exception=True):
                    return social_contact_serializer.save()
            except Exception as e:
                logger.error(
                    f"Unexpected error in get_or_create: {str(e)}", exc_info=True
                )
                raise BaseError(
                    "Error while creating branch contact", original_exception=e
                )
