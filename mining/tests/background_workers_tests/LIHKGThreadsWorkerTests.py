from mining.tests.BaseTestCase import BaseTestCase
from mining.background_workers.LIHKGThreadsWorker import LIHKGThreadsWorker
from mining.background_workers.LIHKGThreadsWorkQueue import LIHKGThreadsWorkQueue
from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager
from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob


class ProcessLIHKGThreadsWorkQueue_IfNoJobInQueueAndAuotFetchJob_ThenFetchJob(BaseTestCase):
    def test(self):
        # arrange
        def dummy(*args, **kwargs):
            return 99

        # used for post-test clean up
        f = LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs
        # replace the actual method call to dummy call as the unit test is to test the
        # work itself rather than the manager
        LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs = dummy

        queue = LIHKGThreadsWorkQueue()
        worker = LIHKGThreadsWorker(queue)
        worker.SetApp(self._app)

        # used for post-test clean up
        before = worker._options.IsAutoFetchLIHKGThreadJobs
        worker._options.IsAutoFetchLIHKGThreadJobs = True

        # act
        worker.ProcessLIHKGThreadsWorkQueue()

        # post-test clean up
        worker._options.IsAutoFetchLIHKGThreadJobs = before
        LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs = f

class ProcessLIHKGThreadsWorkQueue_IfAuotFetchJob_ExceptionHappensOnMgrLevelDoesNotAffectWorkerLevel(BaseTestCase):
    def test(self):
        # arrange
        def dummy(*args, **kwargs):
            raise Exception("dummy exception")

        # used for post-test clean up
        f = LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs
        # replace the actual method call to dummy call as the unit test is to test the
        # work itself rather than the manager
        LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs = dummy

        queue = LIHKGThreadsWorkQueue()
        worker = LIHKGThreadsWorker(queue)
        worker.SetApp(self._app)

        # used for post-test clean up
        before = worker._options.IsAutoFetchLIHKGThreadJobs
        worker._options.IsAutoFetchLIHKGThreadJobs = True

        # act
        worker.ProcessLIHKGThreadsWorkQueue()

        # post-test clean up
        worker._options.IsAutoFetchLIHKGThreadJobs = before
        LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs = f

class ProcessLIHKGThreadsWorkQueue_IfFullFetchJobQueued_ThenWorkProcessed(BaseTestCase):
    def test(self):
        # arrange
        def dummy(*args, **kwargs):
            return True

        # used for post-test clean up
        f = LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs
        # replace the actual method call to dummy call as the unit test is to test the
        # work itself rather than the manager
        LIHKGThreadsManager.FullFetchOneThreadByLIHKGThreadIdWithRetry = dummy

        queue = LIHKGThreadsWorkQueue()
        queue.Put(LIHKGThreadsJob(
            LIHKGThreadId=123,
            page=1,
            isFullFetch=True
        ))
        worker = LIHKGThreadsWorker(queue)
        worker.SetApp(self._app)

        # act
        worker.ProcessLIHKGThreadsWorkQueue()

        # post-test clean up
        LIHKGThreadsManager.FullFetchOneThreadByLIHKGThreadIdWithRetry = f


class ProcessLIHKGThreadsWorkQueue_IfOnePageFetchWorkQueued_ThenWorkProcessed(BaseTestCase):
    def test(self):
        # arrange
        def dummy(*args, **kwargs):
            return True

        # used for post-test clean up
        f = LIHKGThreadsManager.FetchAndQueueLIHKGThreadJobs
        # replace the actual method call to dummy call as the unit test is to test the
        # work itself rather than the manager
        LIHKGThreadsManager.FetchOneThreadPageByLIHKGThreadIdWithRetry = dummy

        queue = LIHKGThreadsWorkQueue()
        queue.Put(LIHKGThreadsJob(
            LIHKGThreadId=123,
            page=1,
            isFullFetch=False
        ))
        worker = LIHKGThreadsWorker(queue)
        worker.SetApp(self._app)

        # act
        worker.ProcessLIHKGThreadsWorkQueue()

        # post-test clean up
        LIHKGThreadsManager.FetchOneThreadPageByLIHKGThreadIdWithRetry = f


