from rest_framework import serializers

from commons.validations.request_validations import validate_obj_or_id


class BranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)


class BranchLocationSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    postal_code = serializers.RegexField(
        regex=r"^\d{5,6}$",
        error_messages={"invalid": "Postal code must be 5 or 6 digits."},
    )
    country = serializers.CharField(max_length=2)


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.RegexField(
        regex=r"^\d{10}$",
        error_messages={"invalid": "Phone number must be exactly 10 digits."},
    )


class CreateBranchSerializer(serializers.Serializer):
    branch = BranchSerializer()
    restaurant = serializers.DictField(required=False)
    restaurant_id = serializers.CharField(required=False)
    location = serializers.DictField(required=False)
    location_id = serializers.CharField(required=False)
    contact = ContactSerializer()

    def validate(self, data):
        validate_obj_or_id(
            data,
            key="restaurant",
            key_id="restaurant_id",
            serializer_class=RestaurantSerializer,
        )
        validate_obj_or_id(
            data,
            key="location",
            key_id="location_id",
            serializer_class=BranchLocationSerializer,
        )
        return data
