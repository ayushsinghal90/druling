import logging

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from .models import Contact
from .serializer import ContactSerializer

logger = logging.getLogger(__name__)


class ContactService(BaseService):
    def __init__(self):
        super().__init__(Contact)

    def get_or_create(self, contact_data):
        """
        Fetches an existing contact by email and phone number, or creates a new one if it doesn't exist.
        """
        try:
            # Try to get the existing contact
            return self.get(contact_data["email"], contact_data["phone_number"])
        except Contact.DoesNotExist:
            # If not found, create a new contact
            contact_serializer = ContactSerializer(data=contact_data)

            if contact_serializer.is_valid(raise_exception=True):
                return contact_serializer.save()
        except Exception as e:
            logger.error(f"Unexpected error in get_or_create: {str(e)}", exc_info=True)
            raise BaseError("Error while creating branch contact", original_exception=e)

    def get(self, email, phone_number):
        """
        Fetches a contact by email and phone number.
        """
        try:
            return Contact.objects.get(email=email, phone_number=phone_number)
        except Contact.DoesNotExist:
            logger.warning(
                f"Contact with email {email} and phone number {phone_number} does not exist."
            )
            raise
        except Exception as e:
            logger.error(f"Error fetching contact: {str(e)}", exc_info=True)
            raise BaseError("Error while fetching branch contact", original_exception=e)
