"""
Work queue class for background LIHKG thread workers.
"""
import queue
from datetime import datetime
import logging
from mining.background_workers.jobs import LIHKGThreadsJob
from mining.config.options.LIHKGThreadsWorkQueueOptions import LIHKGThreadsWorkQueueOptions

class LIHKGThreadsWorkQueue:
    """
    Work queue class for background LIHKG thread workers.
    """

    _options: LIHKGThreadsWorkQueueOptions = None

    def __init__(self):
        self._queue = queue.Queue()
        self._logger = logging.getLogger("flask.app")

    def IsEmpty(self):
        '''
        Calls queue.Queue.empty method to check if the work queue is empty.

        Used by workers to check whether there is work.
        '''

        self.DiscardOldWork()
        return self._queue.empty()

    def Put(self, job: LIHKGThreadsJob):
        '''
        Put the job to the work queue.
        '''

        self.DiscardOldWork()
        self._queue.put(job)

    def Get(self):
        '''
        Get the first work in the work queue.
        '''

        self.DiscardOldWork()
        return self._queue.get_nowait()

    def DiscardOldWork(self):
        '''
        Check whether the first work of the queue is created a long time ago.

        This is called before the Put, Get, IsEmpty methods to
        avoid to many jobs stacking
        '''

        now = datetime.utcnow()
        while not self._queue.empty():
            first_job = self._queue.queue[0]
            if (now - first_job.CreateTime).total_seconds() >= self._options.DiscardJobTimeLimit:
                first_job = self._queue.get()
                self._logger.warning(f"Discarding job {first_job} for being too old.")
            else:
                break

    def QueryAllWork(self):
        '''
        Query all existing work in the queue.
        '''

        return list(self._queue.queue)

    def ClearAllWork(self):
        '''
        Clear all existing work in the queue.
        '''

        while not self._queue.empty():
            self._queue.get_nowait()

# Singleton
# The work queue for handling LIHKG threads jobs.
LIHKGThreadsWORKQUEUE = LIHKGThreadsWorkQueue()
