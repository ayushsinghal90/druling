import logging

from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from email_config.services import BlockedEmailService
from handlers.services.init_onboarding import Onboarding
from ..serializers import RegisterSerializer

User = get_user_model()
logger = logging.getLogger(__name__)


class UserService(BaseService):
    def __init__(self, blocked_email_service=None):
        super().__init__(User)
        self.blocked_email_service = blocked_email_service or BlockedEmailService()

    def get_or_create(self, user_data):
        try:
            user = self.get_by_email(user_data["email"])
            if not user:
                serializer = RegisterSerializer(data=user_data)
                if serializer.is_valid(raise_exception=True):
                    user = serializer.save()
                    Onboarding(user.profile).run()
            return user
        except ValidationError as e:
            logger.warning(f"Validation error while creating user: {str(e)}")
            raise e
        except Exception as e:
            logger.error("Error while creating user", exc_info=True)
            raise BaseError("Error while creating user", original_exception=e)

    def get_by_email(self, email):
        try:
            self.blocked_email_service.verify(email)
            return User.objects.filter(email=email).first()
        except Exception as e:
            logger.error("Error while updating branch location", exc_info=True)
            raise BaseError(
                "Error while updating branch location", original_exception=e
            )
