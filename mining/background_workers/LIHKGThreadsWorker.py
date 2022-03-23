import time
from mining.background_workers.BaseWorker import BaseWorker
from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE

from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager

class LIHKGThreadsWorker(BaseWorker):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def Work(self):

        while True:
            self._logger.info("LIHKGThreads worker working...")
            if not self._queue.IsEmpty():
                LIHKGThreadjob = self._queue.Get()
                LIHKGThreadId, page, isFullFetch = LIHKGThreadjob

                self._logger.info(f"LIHKGThreads worker received job {LIHKGThreadId}")
                with self._app.app_context():

                    lihkgThreadsManager = LIHKGThreadsManager()

                    if isFullFetch:
                        lihkgThreadsManager.FullFetchOneThreadByLIHKGThreadIdWithRetry(LIHKGThreadId, page)
                    else:
                        lihkgThreadsManager.FetchOneThreadPageByLIHKGThreadIdWithRetry(LIHKGThreadId, page)

            time.sleep(self._sleep_time)

lihkgThreadsWorker = LIHKGThreadsWorker(LIHKGThreadsWORKQUEUE)