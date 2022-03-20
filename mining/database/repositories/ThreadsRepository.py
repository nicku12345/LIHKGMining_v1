from mining.database.repositories.BaseRepository import BaseRepository
from mining.database.models.Thread import Thread

class ThreadsRepository(BaseRepository):

    def QueryAllThreads(self):
        return self._db.session.query(Thread).all()

    def QueryThreadByLIHKGThreadId(self, LIHKGThreadId: int):
        return self._db.session.query(Thread).filter_by(LIHKGThreadId=LIHKGThreadId).first()

    def AddThread(self, thread: Thread):
        self.AddAndSave(thread)

    def MergeThread(self, thread: Thread):
        self.MergeAndSave(thread)