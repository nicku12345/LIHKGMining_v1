import logging

class BaseHelper:

    def __init__(self):
        self._logger = logging.getLogger("flask.app")