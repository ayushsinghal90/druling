from rest_framework import serializers
from rest_framework.fields import empty

from file_upload.config import S3_FILE_TYPE_CONFIG
from file_upload.enum.FIleType import FileType


def validate_file_name(value):
    valid_extensions = ["jpg", "jpeg", "png", "gif"]
    if not any(value.lower().endswith(ext) for ext in valid_extensions):
        raise serializers.ValidationError(
            "Invalid file extension. Only photo files are allowed."
        )
    return value


class FileSerializer(serializers.Serializer):
    file_key = serializers.CharField(required=True)

    def __init__(self, instance=None, data=empty, valid_extensions=None, **kwargs):
        super().__init__(instance, data, kwargs)
        self.valid_extensions = valid_extensions

    def validate(self, data):
        if self.valid_extensions:
            validate_file_name(data.get("file_key"))
        return data


class FileUploadSerializer(serializers.Serializer):
    params = serializers.DictField(required=False)
    file_type = serializers.ChoiceField(choices=[e.value for e in FileType])
    files = FileSerializer(many=True, required=True)

    def validate(self, data):
        file_type = data.get("file_type")
        serializer = S3_FILE_TYPE_CONFIG[file_type].serializer
        if serializer:
            serializer(data=data.get("params")).is_valid(raise_exception=True)
        return data
