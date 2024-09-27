from rest_framework import serializers

from .models import QRMenu


class QRMenuSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    ingredients = serializers.JSONField()

    class Meta:
        model = QRMenu
        fields = ["id", "branch", "file_key"]

    def create(self, validated_data):
        return QRMenu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
