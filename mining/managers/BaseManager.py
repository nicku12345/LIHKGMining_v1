"""
Base class of a manager
"""
import logging

class BaseManager:
    """
    Base class of a manager
    """

    def __init__(self):
        self._logger = logging.getLogger("flask.app")
