from functools import wraps


def validate(serializer=None):
    """
    Decorator to validate API requests data using a serializer.

    Args:
        serializer: The serializer class to use for validation.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            if serializer:
                serializer_instance = serializer(data=request.data)
                serializer_instance.is_valid(raise_exception=True)
            return func(self, request, *args, **kwargs)

        return wrapper

    return decorator
