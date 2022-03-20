import logging

class BaseManager:

    def __init__(self):
        self._logger = logging.getLogger("flask.app")