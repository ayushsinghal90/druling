from functools import wraps
import logging

from rest_framework.exceptions import ValidationError

from commons.api.responses import ResponseFactory
from commons.exceptions.BaseError import BaseError

logger = logging.getLogger(__name__)


def handle_api_exceptions(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        try:
            return func(self, request, *args, **kwargs)
        except ValidationError as e:
            logger.error("Invalid Input", e)
            return ResponseFactory.bad_request(message="Invalid Input", data=e.args)
        except BaseError as e:
            return ResponseFactory.server_error(message=e.message, errors=str(e))
        except Exception as e:
            logger.error("Internal Server error", e)
            return ResponseFactory.server_error(message=str(e), data=e.args)

    return wrapper
