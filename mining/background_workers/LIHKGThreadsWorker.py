"""
Concrete worker class for LIHKG threads related functionalities.
"""
import time
from mining.background_workers.BaseWorker import BaseWorker
from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE
from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager

class LIHKGThreadsWorker(BaseWorker):
    """
    Concrete worker class for LIHKG threads related functionalities.
    """

    def Work(self):
        '''
        The main functionality of this worker.

        It periodically pools jobs from the global LIHKGThreadsWORKQUEUE queue and
        handle the job.

        This work should share the same memory with the main-thread of the program so
        that it can access the current app context.
        '''

        while True:
            if not self._queue.IsEmpty():
                self._logger.debug("Jobs polled LIHKGThreads worker...")

                LIHKGThreadsjob = self._queue.Get()
                self._logger.debug(f"LIHKGThreads worker received job {LIHKGThreadsjob}")

                LIHKGThreadId = LIHKGThreadsjob.LIHKGThreadId
                page = LIHKGThreadsjob.page
                isFullFetch = LIHKGThreadsjob.isFullFetch

                with self._app.app_context():

                    lihkgThreadsManager = LIHKGThreadsManager()

                    # full fetch -> fetch all pages of the thread
                    if isFullFetch:
                        lihkgThreadsManager.FullFetchOneThreadByLIHKGThreadIdWithRetry(
                            LIHKGThreadId,
                            page
                        )

                    # else -> fetch only one page
                    else:
                        lihkgThreadsManager.FetchOneThreadPageByLIHKGThreadIdWithRetry(
                            LIHKGThreadId,
                            page
                        )

                self._logger.debug(f"Job {LIHKGThreadsjob} finished")
            elif self._is_auto_fetch_lihkg_thread_jobs:
                self._logger.debug("No job polled from LIHKG thread worker. Trying to fetch for jobs...")

                with self._app.app_context():

                    lihkgThreadsManager = LIHKGThreadsManager()
                    try:
                        num_jobs_added = lihkgThreadsManager.FetchAndQueueLIHKGThreadJobs()
                        self._logger.info(f"Queued {num_jobs_added} jobs.")
                    except Exception as e:
                        self._logger.error(f"No jobs fetched. Reason: {e}")

            time.sleep(self._sleep_time)

'''
Singleton pattern of the background worker.

For now let's just have one worker
'''
lihkgThreadsWorker = LIHKGThreadsWorker(LIHKGThreadsWORKQUEUE)
