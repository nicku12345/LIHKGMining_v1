from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob
from mining.tests.BaseTestCase import BaseTestCase
from time import sleep


class LIHKGThreadsJobs_IfTwoJobsAreCreatedAtTwoTimeStamp_CreateTimeShouldBeDifferent(BaseTestCase):
    def test(self):
        # arrange & act
        job1 = LIHKGThreadsJob(LIHKGThreadId=1, page=1, isFullFetch=False)
        sleep(0.01)
        job2 = LIHKGThreadsJob(LIHKGThreadId=2, page=1, isFullFetch=True)

        # assert
        self.assertTrue(job1.CreateTime < job2.CreateTime)
