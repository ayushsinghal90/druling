from rest_framework import serializers

from branch_location.models import BranchLocation
from branch_location.serializer import BranchLocationSerializer
from commons.serializer.BaseModelSerializer import BaseModelSerializer
from contact.models import Contact
from contact.serializer import ContactSerializer
from file_upload.enum import FileType
from file_upload.services import FileUploadService
from restaurant.models import Restaurant

from .models import Branch


class BranchGetModelSerializer(BaseModelSerializer):
    contact_info = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    restaurant = serializers.SerializerMethodField()
    menu = serializers.SerializerMethodField(required=False)
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = [
            "id",
            "name",
            "img_url",
            "description",
            "location",
            "contact_info",
            "restaurant",
            "menu",
            "is_active",
        ]

    @staticmethod
    def get_contact_info(obj):
        if obj.contact:
            return ContactSerializer(obj.contact).data
        return None

    @staticmethod
    def get_location(obj):
        if obj.location:
            return BranchLocationSerializer(obj.location).data
        return None

    @staticmethod
    def get_restaurant(obj):
        from restaurant.serializer import RestaurantGetSerializer

        if obj.restaurant:
            return RestaurantGetSerializer(
                obj.restaurant, fields=["id", "name", "description"]
            ).data
        return None

    @staticmethod
    def get_img_url(obj):
        if obj.img_url:
            return FileUploadService(FileType.BRANCH_LOGO).get_url(obj.img_url)
        return None

    @staticmethod
    def get_menu(obj):
        from menu.serializer import QRMenuGetSerializer

        if hasattr(obj, "qr_menu") and obj.qr_menu:
            return QRMenuGetSerializer(obj.qr_menu, fields=["id", "theme"]).data
        return None


class BranchCreateModelSerializer(BaseModelSerializer):
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=False,
        allow_null=True,
        source="contact",
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=BranchLocation.objects.all(), required=True, source="location"
    )
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), required=True, source="restaurant"
    )

    class Meta:
        model = Branch
        fields = [
            "id",
            "name",
            "img_url",
            "description",
            "location_id",
            "contact_id",
            "restaurant_id",
            "is_active",
        ]
