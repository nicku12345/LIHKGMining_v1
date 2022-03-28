from mining.tests.BaseTestCase import BaseTestCase
from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob
from mining.background_workers.LIHKGThreadsWorkQueue import LIHKGThreadsWorkQueue

class WorkQueueIsEmptyMethod_IfIsEmpty_ShouldReturnTrue(BaseTestCase):
    def test(self):
        # arrange
        q = LIHKGThreadsWorkQueue()

        # act
        res = q.IsEmpty()

        # assert
        self.assertTrue(res)

class WorkQueueIfPutAndGet_IfHasOnlyOneJob_ShouldGetBackTheJob(BaseTestCase):
    def test(self):
        # arrange
        q = LIHKGThreadsWorkQueue()
        job = LIHKGThreadsJob(LIHKGThreadId=123, page=5, isFullFetch=False)

        # act
        q.Put(job)
        res = q.Get()

        # assert
        self.assertTrue(res.LIHKGThreadId == 123)
        self.assertTrue(res.page == 5)
        self.assertTrue(res.isFullFetch == False)

class WorkQueueGetMethod_IfQueueIsEmpty_ExpectException(BaseTestCase):
    def test(self):
        # arrange
        q = LIHKGThreadsWorkQueue()

        # act
        self.assertRaises(Exception, q.Get)
