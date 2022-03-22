import time
from mining.managers.BaseManager import BaseManager
from mining.managers.ThreadsManager import ThreadsManager
from mining.managers.helpers.LIHKGThreadsHelper import LIHKGThreadsHelper
from mining.managers.helpers.PlaywrightHelper import PlaywrightHelper

class LIHKGThreadsManager(BaseManager):

    def __init__(self):
        super().__init__()
        self._threadsManager = ThreadsManager()
        self._lihkgThreadsHelper = LIHKGThreadsHelper()
        self._playwrightHelper = PlaywrightHelper()

    def FullFetchOneThreadByLIHKGThreadId(self, LIHKGThreadId: int, page: int):
        while True:
            try:
                success, num_msgs_fetched = self.FetchOneThreadPageByLIHKGThreadId(LIHKGThreadId, page)
                if success:
                    if num_msgs_fetched == 0:
                        break
                    else:
                        page += 1

            except Exception as e:
                self._logger.warn(f"Encountered exception: {e}")

            time.sleep(1)

    def FetchOneThreadPageByLIHKGThreadId(self, LIHKGThreadId: int, page: int):
        website_url, target_api_url_pref = self._lihkgThreadsHelper.GetFetchThreadWebsiteAndApiUrlPrefix(LIHKGThreadId, page)

        self._logger.info(f"Received fetch on LIHKGThreadId: {LIHKGThreadId}, Page: {page}")
        self._logger.debug(f"Generated website url: {website_url}")
        self._logger.debug(f"Generated API url prefix: {target_api_url_pref}")
        self._logger.info("Now fetching...")
        
        lihkg_thread = self._playwrightHelper.FetchTargetApiByVisitingWebsite(website_url, target_api_url_pref)
        if not self._lihkgThreadsHelper.IsResponseSuccess(lihkg_thread):
            self._logger.warn(f"Failed fetch on LIHKGThreadId: {LIHKGThreadId}, Page: {page}")
            return False, 0
        
        thread = self._lihkgThreadsHelper.ConvertToThread(lihkg_thread)
        user = self._lihkgThreadsHelper.ConvertToUser(lihkg_thread)
        messages = self._lihkgThreadsHelper.ConvertToMessages(lihkg_thread)
        users = self._lihkgThreadsHelper.ConvertToUsers(lihkg_thread)

        self._logger.debug(f"Fetched thread: {thread}")
        self._logger.debug(f"Fetched user: {user}")
        self._logger.debug(f"Fetched messages count: {len(messages)}")
        self._logger.info(f"Persisting the found thread to database")

        self._threadsManager.AddThread(thread, user, messages, users)

        return True, len(messages)