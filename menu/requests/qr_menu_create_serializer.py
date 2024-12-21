from rest_framework import serializers


class CreateQRMenuSerializer(serializers.Serializer):
    branch_id = serializers.CharField(required=True)
    file_key = serializers.CharField(required=True)
