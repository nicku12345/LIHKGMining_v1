"""
Base class of a repository.
"""
import logging
from mining.database import db

class BaseRepository:
    """
    Base class of a repository.
    """

    def __init__(self):
        self._db = db
        self._logger = logging.getLogger("flask.app")

    def Save(self):
        '''
        Calls the db.session.commit method to save changes which have checked in.
        '''
        self._db.session.commit()

    def MergeAndSave(self, obj):
        '''
        Calls the db.session.merge method and save the changes.
        '''
        self._db.session.merge(obj)
        self.Save()

    def AddAndSave(self, obj):
        '''
        Calls the db.session.add method and save the changes.
        '''
        self._db.session.add(obj)
        self.Save()
