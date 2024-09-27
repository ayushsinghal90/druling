import traceback


class BaseError(Exception):
    def __init__(self, message, original_exception=None):
        self.message = message
        self.original_exception = original_exception

        if original_exception:
            self.traceback = traceback.format_exception(
                type(original_exception),
                original_exception,
                original_exception.__traceback__,
            )
        else:
            self.traceback = None

        super().__init__(self.message)

    def __str__(self):
        if self.original_exception:
            return (
                f"{self.message}\n"
                f"Original Exception: {type(self.original_exception).__name__} - {str(self.original_exception)}\n"
                f"Traceback:\n{''.join(self.traceback)}"
            )
        return self.message

    def __repr__(self):
        if self.original_exception:
            return (
                f"<BaseError(message={self.message}, "
                f"original_exception={type(self.original_exception).__name__})>"
            )
        return f"<BaseError(message={self.message})>"
