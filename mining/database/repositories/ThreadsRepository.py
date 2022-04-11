"""
Concrete repository for thread entities related functionalities.
"""
from sqlalchemy.orm import joinedload, noload
from mining.database.repositories.BaseRepository import BaseRepository
from mining.database.models.Thread import Thread
from mining.database.models.Message import Message

class ThreadsRepository(BaseRepository):
    """
    Concrete repository for thread entities related functionalities.
    """

    def QueryAllThreads(self, skip_messages=False):
        '''
        Returns a list of all threads in the attached Threads table.
        '''
        if not skip_messages:
            return self._db.session.query(Thread).options(
                joinedload(Thread.Messages).joinedload(Message.User)
            ).all()
        else:
            return self._db.session.query(Thread).options(
                noload(Thread.Messages)
            ).all()

    def QueryThreadByLIHKGThreadId(self, LIHKGThreadId: int):
        '''
        Returns the thread having the LIHKGThreadId provided.

        Returns None otherwise.
        '''
        return self._db.session.query(Thread).filter_by(LIHKGThreadId=LIHKGThreadId).first()

    def AddThread(self, thread: Thread):
        '''
        Calls the SQLAlchemy db.session.add method and commits the changes
        '''
        self.AddAndSave(thread)

    def MergeThread(self, thread: Thread):
        '''
        Calls the SQLAlchemy db.session.merge method and commits the changes
        '''
        self.MergeAndSave(thread)
