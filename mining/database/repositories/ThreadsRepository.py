from mining.database.repositories.BaseRepository import BaseRepository
from mining.database.models.Thread import Thread

class ThreadsRepository(BaseRepository):

    def QueryAllThreads(self):
        '''
        Returns a list of all threads in the attached Threads table.
        '''
        return self._db.session.query(Thread).all()

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