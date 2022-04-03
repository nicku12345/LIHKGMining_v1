from mining.tests.BaseTestCase import BaseTestCase
from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager
from mining.tests._mock_objects.MockPlaywright import *
from mining.tests._mock_data.examples.lihkg_api_v2_thread_example import example_json_response
from mining.background_workers.LIHKGThreadsWorkQueue import LIHKGThreadsWORKQUEUE


class FullFetchOneThreadByLIHKGThreadIdWithRetry_IfResponseIfOk_ThenNoErrorIsThrown(BaseTestCase):
    def test(self):
        # arrange
        def MockFetchTargetApiByVisitingWebsite(website_url, target_api_url_prefix):
            return example_json_response.copy()

        mgr = LIHKGThreadsManager()
        mgr._playwrightHelper.FetchTargetApiByVisitingWebsite = MockFetchTargetApiByVisitingWebsite

        # act & assert
        mgr.FullFetchOneThreadByLIHKGThreadIdWithRetry(LIHKGThreadId=1, page_start=1, page_end=1)

class FullFetchOneThreadByLIHKGThreadIdWithRetry_IfResponseFail_ThenNoErrorIsThrown(BaseTestCase):
    def test(self):
        # arrange
        def MockFetchTargetApiByVisitingWebsite(website_url, target_api_url_prefix):
            return {"success": 0}

        mgr = LIHKGThreadsManager()
        mgr._playwrightHelper.FetchTargetApiByVisitingWebsite = MockFetchTargetApiByVisitingWebsite

        # act & assert
        mgr.FullFetchOneThreadByLIHKGThreadIdWithRetry(LIHKGThreadId=1, page_start=1, page_end=1)

class FetchAndQueueLIHKGThreadJobs_IfResponseFail_ThenNoJobIsQueued(BaseTestCase):
    def test(self):
        # arrange
        def MockFetchTargetApiByVisitingWebsite(website_url, target_api_url_prefix):
            return {"success": 0}

        mgr = LIHKGThreadsManager()
        mgr._playwrightHelper.FetchTargetApiByVisitingWebsite = MockFetchTargetApiByVisitingWebsite

        # act
        res = mgr.FetchAndQueueLIHKGThreadJobs()

        # assert
        self.assertTrue(res == 0)

class FetchAndQueueLIHKGThreadJobs_IfResponseOk_ThenJobsAreQueued(BaseTestCase):
    def test(self):
        # arrange
        self.assertTrue(LIHKGThreadsWORKQUEUE.IsEmpty())
        def MockFetchTargetApiByVisitingWebsite(website_url, target_api_url_prefix):
            return {
                "success": 1,
                "response": {
                    "items": [
                        {
                            "thread_id": 980,
                        }
                    ]
                }
            }

        mgr = LIHKGThreadsManager()
        mgr._playwrightHelper.FetchTargetApiByVisitingWebsite = MockFetchTargetApiByVisitingWebsite

        # act
        mgr.FetchAndQueueLIHKGThreadJobs()

        # assert
        self.assertFalse(LIHKGThreadsWORKQUEUE.IsEmpty())

        # post test clean up
        while not LIHKGThreadsWORKQUEUE.IsEmpty():
            LIHKGThreadsWORKQUEUE.Get()
