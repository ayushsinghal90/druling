from rest_framework import serializers


class PlanSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    duration = serializers.IntegerField()
