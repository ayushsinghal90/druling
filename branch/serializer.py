from rest_framework import serializers

from branch_location.models import BranchLocation
from contact.models import Contact
from restaurant.models import Restaurant

from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
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
