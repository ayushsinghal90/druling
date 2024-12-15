from rest_framework import serializers

from .models import BranchLocation


class BranchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchLocation
        fields = ["id", "address", "city", "state", "postal_code", "country"]
