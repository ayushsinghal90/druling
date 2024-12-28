from rest_framework import serializers


def validate_file_name(value):
    valid_extensions = ["jpg", "jpeg", "png", "gif"]
    if not any(value.lower().endswith(ext) for ext in valid_extensions):
        raise serializers.ValidationError(
            "Invalid file extension. Only photo files are allowed."
        )
    return value


class MenuFileSerializer(serializers.Serializer):
    file_key = serializers.CharField(required=True)
    order = serializers.IntegerField(required=False)
    category = serializers.CharField(required=False)

    def validate(self, data):
        validate_file_name(data.get("file_key"))
        return data
