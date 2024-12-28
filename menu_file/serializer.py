from rest_framework import serializers

from commons.serializer.BaseModelSerializer import BaseModelSerializer
from menu.models import QRMenu

from .models import MenuFile
from .utils import get_url


class MenuFileGetSerializer(BaseModelSerializer):
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=QRMenu.objects.all(), required=True, source="menu"
    )

    class Meta:
        model = MenuFile
        fields = ["id", "menu_id", "file_url", "order", "category"]

    @staticmethod
    def get_file_url(obj):
        if obj.file_key:
            return get_url(obj.menu.branch_id, obj.file_key)
        return None


class MenuFileCreateSerializer(BaseModelSerializer):
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=QRMenu.objects.all(), required=True, source="menu"
    )

    class Meta:
        model = MenuFile
        fields = ["id", "menu_id", "file_key", "order", "category"]
