import playwright.sync_api as pw
from playwright.sync_api import Playwright, sync_playwright
from mining.managers.helpers.BaseHelper import BaseHelper
from mining.util.Exceptions import *


class PlaywrightHelper(BaseHelper):

    def __init__(self):
        super().__init__()

    def FetchTargetApiByVisitingWebsite(self, website_url: str, target_api_uri_prefix: str):
        p = sync_playwright().start()
        browser = p.webkit.launch()
        page = browser.new_page()

        response = None

        def UpdateResponseIfIsTargetApi(res: pw.Response):
            nonlocal response, target_api_uri_prefix

            resource_type = res.request.resource_type.lower()
            if (resource_type != "xhr" and resource_type != "fetch"):
                return

            if res.request.url.startswith(target_api_uri_prefix):
                if response != None:
                    raise ExternalApiIsNotUniqueException(f"Found multiple APIs having {target_api_uri_prefix} as prefix")

                if not res.ok:
                    raise ExternalApiRequestException(f"External API {res.request.url} failed.")

                response = res.json()

        page.on("response", lambda res: UpdateResponseIfIsTargetApi(res))
        page.goto(website_url, timeout=0, wait_until="networkidle")

        if response == None:
            self._logger.error(f"No xhr or fetch response found. Website={website_url}. Target_api prefix={target_api_uri_prefix}")
        else:
            self._logger.info(f"Successful fetch on website={website_url}, API prefix={target_api_uri_prefix}")

        browser.close()
        p.stop()

        return response



