"""
Concete manager class for LIHKG threads related functionalities.
"""
import time
import random
from mining.managers.BaseManager import BaseManager
from mining.managers.ThreadsManager import ThreadsManager
from mining.managers.helpers.LIHKGThreadsHelper import LIHKGThreadsHelper
from mining.managers.helpers.PlaywrightHelper import PlaywrightHelper
from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE
from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob

class LIHKGThreadsManager(BaseManager):
    """
    Concrete manager class for LIHKG threads related functionalities.
    """

    def __init__(self):
        super().__init__()
        self._threadsManager = ThreadsManager()
        self._lihkgThreadsHelper = LIHKGThreadsHelper()
        self._playwrightHelper = PlaywrightHelper()

        # Used for fetching threads. The fetch will retry on failure,
        # and stop once reaching this threshold
        self._max_failure_cnt = 3

        # Used for fetching threads. Introduces a sleep between page fetches with
        # duration randomly chosen in the open interval (0, _sleep_time).
        # Its purpose is to create a more dynamic and less machinery behavior.
        self._sleep_time = 3

    def FullFetchOneThreadByLIHKGThreadIdWithRetry(
            self,
            LIHKGThreadId: int,
            page_start: int = 1,
            page_end: int = 40):
        '''
        Performs a full fetch for one LIHKG thread with retrials.

        :param LIHKGThreadId: The LIHKG thread id.
        :param page_start: The number of page to start fetching.
        :param page_end: The number of page to stop fetching. Default is 40.
        '''
        for page in range(page_start, page_end + 1):

            success, num_msgs_fetched \
                = self.FetchOneThreadPageByLIHKGThreadIdWithRetry(LIHKGThreadId, page)

            if success and num_msgs_fetched == 0:
                break
            time.sleep(random.uniform(0, self._sleep_time))

    def FetchOneThreadPageByLIHKGThreadIdWithRetry(self, LIHKGThreadId: int, page: int):
        '''
        Performs a fetch for one LIHKG thread page with retrials.

        :param LIHKGThreadId: The LIHKG thread id.
        :param page: The number of page to fetch.
        :return: (success: bool, number_messages_fetched: int)
        '''
        failure_cnt = 0
        while True:
            try:
                success, num_msgs_fetched = \
                    self.FetchOneThreadPageByLIHKGThreadId(LIHKGThreadId, page)

                if success:
                    return success, num_msgs_fetched

            except Exception as e:
                self._logger.warning(f"Encountered exception: {e}")
                return False, 0

            failure_cnt += 1
            if failure_cnt >= self._max_failure_cnt:
                self._logger.info(f"Putting thread: {LIHKGThreadId}, "
                                  f"page: {page} to queue for latter re-processing.")

                job = LIHKGThreadsJob(
                    LIHKGThreadId=LIHKGThreadId,
                    page=page,
                    isFullFetch=False
                )
                LIHKGThreadsWORKQUEUE.Put(job)
                return False, 0

            time.sleep(random.uniform(0, self._sleep_time))


    def FetchOneThreadPageByLIHKGThreadId(self, LIHKGThreadId: int, page: int):
        '''
        Performs a single page fetch for a LIHKG thread.

        :param LIHKGThreadId: The LIHKG thread id.
        :param page: The number of page to fetch.
        :return: (success: bool, number_messages_fetched: int)
        '''
        website_url, target_api_url_pref = \
            self._lihkgThreadsHelper.GetFetchThreadWebsiteAndApiUrlPrefix(LIHKGThreadId, page)

        self._logger.info(f"Received fetch on LIHKGThreadId: {LIHKGThreadId}, Page: {page}")
        self._logger.debug(f"Generated website url: {website_url}")
        self._logger.debug(f"Generated API url prefix: {target_api_url_pref}")
        self._logger.info("Now fetching...")

        lihkg_thread = \
            self._playwrightHelper.FetchTargetApiByVisitingWebsite(website_url, target_api_url_pref)
        if not self._lihkgThreadsHelper.IsResponseSuccess(lihkg_thread):
            self._logger.warning(f"Failed fetch on LIHKGThreadId: {LIHKGThreadId}, Page: {page}")
            return False, 0

        thread = self._lihkgThreadsHelper.ConvertToThread(lihkg_thread)
        user = self._lihkgThreadsHelper.ConvertToUser(lihkg_thread)
        messages = self._lihkgThreadsHelper.ConvertToMessages(lihkg_thread)
        users = self._lihkgThreadsHelper.ConvertToUsers(lihkg_thread)

        self._logger.debug(f"Fetched thread: {thread}")
        self._logger.debug(f"Fetched user: {user}")
        self._logger.debug(f"Fetched messages count: {len(messages)}")
        self._logger.info("Persisting the found thread to database")

        self._threadsManager.AddThread(thread, user, messages, users)

        return True, len(messages)

    def FetchAndQueueLIHKGThreadJobs(self):
        '''
        Fetch the threads listing on LIHKG Category 1 page.

        Add the jobs to work queue.
        '''

        website_url, target_api_url_pref = \
            self._lihkgThreadsHelper.GetLIHKGThreadJobWebsiteAndApiUrlPrefix()

        self._logger.info("Trying to fetch for LIHKG thread jobs")
        lihkg_category_response = \
            self._playwrightHelper.FetchTargetApiByVisitingWebsite(website_url, target_api_url_pref)

        if not self._lihkgThreadsHelper.IsResponseSuccess(lihkg_category_response):
            self._logger.warning("Fetch job failed!")
            return 0

        jobs = self._lihkgThreadsHelper.ConvertToJobs(lihkg_category_response)
        self._logger.debug(f"Received {len(jobs)} jobs")
        self._logger.debug(f"LIHKGThreadIds of the jobs: {','.join(job.LIHKGThreadId for job in jobs)}")

        for job in jobs:
            LIHKGThreadsWORKQUEUE.Put(job)

        return len(jobs)
