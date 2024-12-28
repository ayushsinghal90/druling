from rest_framework import serializers

from branch.models import Branch


def validate_file_name(value):
    valid_extensions = ["jpg", "jpeg", "png", "gif"]
    if not any(value.lower().endswith(ext) for ext in valid_extensions):
        raise serializers.ValidationError(
            "Invalid file extension. Only photo files are allowed."
        )
    return value


class CreateQRMenuSerializer(serializers.Serializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=True, source="branch"
    )
    file_key = serializers.CharField(required=True)

    def validate(self, data):
        validate_file_name(data.get("file_key"))
        return data


class MenuFileNameSerializer(serializers.Serializer):
    file_key = serializers.CharField(required=True)

    def validate(self, data):
        validate_file_name(data.get("file_key"))
        return data
