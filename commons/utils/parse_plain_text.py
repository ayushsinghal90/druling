import json

from rest_framework.parsers import BaseParser


class PlainTextParser(BaseParser):
    """
    Plain text parser that handles SNS messages sent as text/plain
    """

    media_type = "text/plain"

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        try:
            return json.loads(stream.read().decode("utf-8"))
        except json.JSONDecodeError as e:
            raise e
