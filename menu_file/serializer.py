from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from file_upload.enum.FIleType import FileType
from file_upload.services import FileUploadService
from menu.models import QRMenu

from .models import MenuFile


class MenuFileGetSerializer(BaseModelSerializer):
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=QRMenu.objects.all(), required=True, source="menu"
    )
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = MenuFile
        fields = ["id", "menu_id", "file_url", "order", "category"]

    @staticmethod
    def get_file_url(obj):
        if obj.file_key:
            return FileUploadService(FileType.QR_MENU).get_url(
                obj.file_key, path_params={"branch_id": obj.menu.branch_id}
            )
        return None


class MenuFileCreateSerializer(BaseModelSerializer):
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=QRMenu.objects.all(), required=True, source="menu"
    )

    class Meta:
        model = MenuFile
        fields = ["id", "menu_id", "file_key", "order", "category"]
