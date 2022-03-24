"""
Base class of a helper
"""
import logging


class BaseHelper:
    """
    Base class of a helper
    """

    def __init__(self):
        self._logger = logging.getLogger("flask.app")
