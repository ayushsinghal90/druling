from rest_framework import serializers

from branch.serializer import BranchGetSerializer
from contact.models import Contact
from contact.serializer import ContactSerializer

from .models import Restaurant


class RestaurantGetSerializer(serializers.ModelSerializer):
    branches = BranchGetSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "contact_info", "branches"]

    @staticmethod
    def get_contact_info(obj):
        if obj.contact:
            return ContactSerializer(obj.contact).data
        return None


class RestaurantCreateSerializer(serializers.ModelSerializer):
    contact_id = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=False,
        allow_null=True,
        source="contact",
    )

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "contact_id"]

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
