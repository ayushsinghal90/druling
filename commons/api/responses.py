from rest_framework import status
from rest_framework.response import Response


class BaseResponse(Response):
    def __init__(self, data=None, message=None, status=None, **kwargs):
        super().__init__(data=None, status=status)
        self.data = {
            "success": status is None or status < 400,
            "message": message,
            "data": data,
        }
        self.data.update(kwargs)


class SuccessResponse(BaseResponse):
    def __init__(self, data=None, message="Operation successful", **kwargs):
        super().__init__(
            data=data, message=message, status=status.HTTP_200_OK, **kwargs
        )


class CreatedResponse(BaseResponse):
    def __init__(self, data=None, message="Resource created successfully", **kwargs):
        super().__init__(
            data=data, message=message, status=status.HTTP_201_CREATED, **kwargs
        )


class BadRequestResponse(BaseResponse):
    def __init__(self, data=None, message="Bad requests", errors=None, **kwargs):
        super().__init__(
            data=data,
            message=message,
            errors=errors,
            status=status.HTTP_400_BAD_REQUEST,
            **kwargs
        )


class NotFoundResponse(BaseResponse):
    def __init__(self, data=None, message="Resource not found", **kwargs):
        super().__init__(
            data=data, message=message, status=status.HTTP_404_NOT_FOUND, **kwargs
        )


class UnauthorizedResponse(BaseResponse):  # New class for unauthorized response
    def __init__(self, data=None, message="Unauthorized access", **kwargs):
        super().__init__(
            data=data, message=message, status=status.HTTP_401_UNAUTHORIZED, **kwargs
        )


class ServerErrorResponse(BaseResponse):
    def __init__(self, data=None, message="Internal server error", **kwargs):
        super().__init__(
            data=data,
            message=message,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            **kwargs
        )


class ResponseFactory:
    @staticmethod
    def success(data=None, message="Operation successful", **kwargs):
        return SuccessResponse(data=data, message=message, **kwargs)

    @staticmethod
    def created(data=None, message="Resource created successfully", **kwargs):
        return CreatedResponse(data=data, message=message, **kwargs)

    @staticmethod
    def bad_request(data=None, message="Bad requests", errors=None, **kwargs):
        return BadRequestResponse(data=data, message=message, errors=errors, **kwargs)

    @staticmethod
    def not_found(data=None, message="Resource not found", errors=None, **kwargs):
        return NotFoundResponse(data=data, message=message, errors=errors, **kwargs)

    @staticmethod
    def unauthorized(
        data=None, message="Unauthorized access", **kwargs
    ):  # Factory method
        return UnauthorizedResponse(data=data, message=message, **kwargs)

    @staticmethod
    def server_error(data=None, message="Internal server error", errors=None, **kwargs):
        return ServerErrorResponse(data=data, message=message, errors=errors, **kwargs)
