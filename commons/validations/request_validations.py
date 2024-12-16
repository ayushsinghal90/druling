from rest_framework import serializers


def validate_obj_or_id(data, key=None, key_id=None, serializer_class=None):
    """
    Perform cross-field validation for obj and obj_id.
    """
    key_value = data.get(key)
    key_id_value = data.get(key_id)

    # Ensure either is provided, but not both
    if not key_value and not key_id_value:
        raise serializers.ValidationError(
            {key: f"Either {key} or {key_id} must be provided."}
        )
    if key_value and key_id_value:
        raise serializers.ValidationError(
            {key: f"Provide only one of {key} or {key_id}, not both."}
        )

    # If obj value is provided, validate its structure
    if key_value:
        nested_serializer = serializer_class(data=key_value)
        if not nested_serializer.is_valid(raise_exception=True):
            raise serializers.ValidationError({key: nested_serializer.errors})
