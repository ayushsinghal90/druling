from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    """
    A base serializer class that can be extended by other serializers.
    It can include common functionality like custom validation or dynamic fields.
    """

    def __init__(self, *args, **kwargs):
        # Dynamically set fields if passed in kwargs
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        # If 'fields' is provided, limit the serializer fields to the specified ones
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
