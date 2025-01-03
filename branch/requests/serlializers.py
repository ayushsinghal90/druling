from rest_framework import serializers


class BranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(
        max_length=500, required=False, allow_blank=True
    )
    img_url = serializers.CharField(max_length=200, required=False, allow_blank=True)
