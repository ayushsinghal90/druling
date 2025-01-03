from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from contact.models import Contact
from contact.serializer import ContactSerializer
from file_upload.enum import FileType
from file_upload.services import FileUploadService
from user.models import User

from .models import Profile


class ProfileGetSerializer(BaseModelSerializer):
    contact_info = serializers.SerializerMethodField()
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "contact_info", "id", "img_url"]

    @staticmethod
    def get_contact_info(obj):
        if obj.contact:
            return ContactSerializer(obj.contact).data
        return None

    @staticmethod
    def get_img_url(obj):
        if obj.img_url:
            return FileUploadService(FileType.USER_PROFILE).get_url(obj.img_url)
        return None


class ProfileSerializer(BaseModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True, source="profile"
    )
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(), required=True, source="contact"
    )

    class Meta:
        model = Profile
        fields = ["id", "user_id", "contact_id", "img_url"]
