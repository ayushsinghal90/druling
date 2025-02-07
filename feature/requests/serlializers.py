from rest_framework import serializers


class FeatureSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200)
    limit = serializers.IntegerField(default=0)
    is_active = serializers.BooleanField(default=True)
