from rest_framework import serializers


class BranchLocationSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    postal_code = serializers.RegexField(
        regex=r"^\d{5,6}$",
        error_messages={"invalid": "Postal code must be 5 or 6 digits."},
    )
    country = serializers.CharField(max_length=2)
