from rest_framework import serializers

from branch.requests.serlializers import BranchSerializer
from branch_location.requests.serlializers import BranchLocationSerializer
from commons.validations.request_validations import validate_obj_or_id
from contact.requests.serlializers import ContactSerializer
from restaurant.requests.serlializers import RestaurantSerializer


class BranchCreateSerializer(serializers.Serializer):
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
