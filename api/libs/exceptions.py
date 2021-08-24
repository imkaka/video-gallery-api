import logging

# django/rest_framework imports
from rest_framework.exceptions import ParseError

logger = logging.getLogger('api')


class ParseException(ParseError):
    def __init__(self, detail=None, code=None, errors=None):
        if errors:
            logger.info(errors)
        return super().__init__(detail, code)
