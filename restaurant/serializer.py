from rest_framework import serializers

from contact.models import Contact

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        required=False,
        allow_null=True,
        source="contact",
    )

    class Meta:
        model = Restaurant
        fields = ["id", "name", "description", "contact_id"]
