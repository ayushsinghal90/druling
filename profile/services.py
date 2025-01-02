from django.db import transaction

from commons.service.BaseService import BaseService
from contact.services import ContactService
from profile.models import Profile
from profile.serializer import ProfileSerializer


class ProfileService(BaseService):
    def __init__(self, contact_service=None):
        super().__init__(Profile)
        self.contact_service = contact_service or ContactService()

    def update(self, profile_id, data):
        with transaction.atomic():
            profile = self.get_by_id(profile_id)

            contact_data = data.pop("contact_info")
            if contact_data:
                contact = self.contact_service.get_or_create(contact_data)
                data["contact_id"] = contact.id

            first_name = data.pop("first_name")
            last_name = data.pop("last_name")
            user = profile.user
            if first_name != user.first_name or last_name != user.last_name:
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            profile_serializer = ProfileSerializer(profile, data=data, partial=True)

            if profile_serializer.is_valid(raise_exception=True):
                return profile_serializer.save()
