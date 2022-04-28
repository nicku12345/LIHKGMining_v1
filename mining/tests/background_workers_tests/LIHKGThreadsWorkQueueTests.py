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

# This test is important in the sense that we add jobs with smaller LIHKGThreadIds
# Please check FetchAndQueueLIHKGThreadJobs for the strategy
class WorkQueueGetMethod_ShouldBeFIFO(BaseTestCase):
    def test(self):
        # arrange
        q = LIHKGThreadsWorkQueue()
        job1 = LIHKGThreadsJob(LIHKGThreadId=1, page=5, isFullFetch=False)
        job2 = LIHKGThreadsJob(LIHKGThreadId=2, page=5, isFullFetch=False)

        # act
        q.Put(job1)
        q.Put(job2)

        res1 = q.Get()
        res2 = q.Get()

        # assert
        self.assertTrue(res1.LIHKGThreadId == 1)
        self.assertTrue(res2.LIHKGThreadId == 2)

class WorkQueueGetMethod_IfQueueIsEmpty_ExpectException(BaseTestCase):
    def test(self):
        # arrange
        q = LIHKGThreadsWorkQueue()

        # act
        self.assertRaises(Exception, q.Get)
