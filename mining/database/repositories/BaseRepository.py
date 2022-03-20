from typing import Any
import logging
from mining.database import db

class BaseRepository:

    def __init__(self):
        self._db = db
        self._logger = logging.getLogger("flask.app")

    def Save(self):
        self._db.session.commit()

    def MergeAndSave(self, object: Any):
        self._db.session.merge(object)
        self.Save()

    def AddAndSave(self, object: Any):
        self._db.session.add(object)
        self.Save()