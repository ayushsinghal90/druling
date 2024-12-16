from functools import wraps

from commons.api.responses import ResponseFactory
from commons.exceptions.BaseError import BaseError
from commons.exceptions.Errors import (
    InvalidInputError,
    NotFoundError,
    PermissionDeniedError,
    UnauthorizedError,
    ValidationError,
)


def handle_api_exceptions(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        try:
            return func(self, request, *args, **kwargs)
        except (ValidationError, InvalidInputError, NotFoundError) as e:
            return ResponseFactory.bad_request(message=e.message)
        except (UnauthorizedError, PermissionDeniedError) as e:
            return ResponseFactory.unauthorized(message=e.message)
        except BaseError as e:
            return ResponseFactory.server_error(message=e.message)
        except Exception as e:
            return ResponseFactory.server_error(message=str(e))

    return wrapper
