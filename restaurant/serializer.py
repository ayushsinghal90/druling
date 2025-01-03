from rest_framework import serializers

from branch.serializer import BranchGetModelSerializer
from commons.serializer.BaseModelSerializer import BaseModelSerializer
from contact.models import Contact
from contact.serializer import ContactSerializer
from file_upload.enum import FileType
from file_upload.services import FileUploadService

from .models import Restaurant


class RestaurantGetSerializer(BaseModelSerializer):
    branches = BranchGetModelSerializer(
        many=True,
        fields=[
            "id",
            "name",
            "description",
            "location",
            "contact_info",
            "menu",
            "img_url",
        ],
    )
    contact_info = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ["id", "name", "img_url", "description", "contact_info", "branches"]

    @staticmethod
    def get_contact_info(obj):
        if obj.contact:
            return ContactSerializer(obj.contact).data
        return None

    @staticmethod
    def get_img_url(obj):
        if obj.img_url:
            return FileUploadService(FileType.RESTAURANT_LOGO).get_url(obj.img_url)
        return None


class RestaurantCreateSerializer(BaseModelSerializer):
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=False,
        allow_null=True,
        source="contact",
    )

    class Meta:
        model = Restaurant
        fields = ["id", "name", "img_url", "description", "contact_id"]

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
