from functools import wraps
from commons.middleware.api_exception_handler import handle_exceptions
from commons.middleware.api_validation import validate


def api_handler(serializer=None, handle_exception=True):
    """
    Decorator to dynamically apply @handle_exceptions and/or @validate.

    Args:
        serializer: The serializer class to use for requests validation (optional).
        handle_exception: Boolean indicating whether to apply @handle_api_exceptions (default: True).
    """

    def decorator(func):
        decorated_func = func

        # Apply decorators in the correct order
        if serializer:
            decorated_func = validate(serializer)(decorated_func)

        if handle_exception:
            decorated_func = handle_exceptions(decorated_func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return decorated_func(*args, **kwargs)

        return wrapper

    return decorator
