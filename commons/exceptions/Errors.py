from commons.exceptions.BaseError import BaseError


class InvalidInputError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class ValidationError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class NotFoundError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class UnauthorizedError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class PermissionDeniedError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class DatabaseError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class TimeoutError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class ServiceUnavailableError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class ConflictError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)


class ExternalServiceError(BaseError):
    def __init__(self, message, original_exception=None):
        super().__init__(message, original_exception)
