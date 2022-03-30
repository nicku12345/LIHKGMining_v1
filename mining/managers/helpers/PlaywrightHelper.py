"""
Concrete helper for playwright related functionalities.
"""
import playwright.sync_api as pw
from playwright.sync_api import sync_playwright
from mining.managers.helpers.BaseHelper import BaseHelper
from mining.util.Exceptions import *


class PlaywrightHelper(BaseHelper):
    """
    Concrete helper for playright related functionalities.
    """

    def __init__(self):
        super().__init__()
        self._playwright = None

    def GetPlaywright(self):
        '''
        Get a playwright instance.

        One helper instance can have at most one playwright instance
        '''
        if self._playwright is not None:
            return self._playwright

        self._playwright = sync_playwright().start()
        return self._playwright

    def StopPlaywright(self):
        '''
        Stop a playwright instance
        '''
        self._playwright.stop()

    def FetchTargetApiByVisitingWebsite(self, website_url: str, target_api_uri_prefix: str):
        '''
        Visit the website and fetch response with the target api uri prefix.
        '''
        p = self.GetPlaywright()
        browser = p.webkit.launch()
        page = browser.new_page()

        response = None

        def UpdateResponseIfIsTargetApi(res: pw.Response):
            nonlocal response, target_api_uri_prefix

            resource_type = res.request.resource_type.lower()
            if resource_type not in ("xhr", "fetch"):
                return

            if res.request.url.startswith(target_api_uri_prefix):
                if response is not None:
                    raise ExternalApiIsNotUniqueException(f"Found multiple APIs having {target_api_uri_prefix} as prefix")

                if not res.ok:
                    raise ExternalApiRequestException(f"External API {res.request.url} failed.")

                response = res.json()

        page.on("response", UpdateResponseIfIsTargetApi)
        page.goto(website_url, timeout=0, wait_until="networkidle")

        if response is None:
            self._logger.error(f"No xhr or fetch response found. Website={website_url}. Target_api prefix={target_api_uri_prefix}")
        else:
            self._logger.info(f"Successful fetch on website={website_url}, API prefix={target_api_uri_prefix}")

        browser.close()
        self.StopPlaywright()

        return response
