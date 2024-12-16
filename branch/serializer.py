from rest_framework import serializers

from branch_location.models import BranchLocation
from branch_location.serializer import BranchLocationSerializer
from commons.serializer.BaseModelSerializer import BaseModelSerializer
from contact.models import Contact
from contact.serializer import ContactSerializer
from restaurant.models import Restaurant

from .models import Branch


class BranchGetModelSerializer(BaseModelSerializer):
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source="restaurant", required=True
    )
    contact_info = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = ["id", "name", "location", "contact_info", "restaurant_id"]

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
        fields = ["id", "name", "location_id", "contact_id", "restaurant_id"]
