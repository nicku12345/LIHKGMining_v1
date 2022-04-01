from mining.tests._mock_objects.MockPlaywright import *
from mining.tests.BaseTestCase import BaseTestCase
from mining.managers.helpers.PlaywrightHelper import PlaywrightHelper


class FetchTargetApiByVisitingWebsite_IfNoResponse_ReturnNone(BaseTestCase):
    def test(self):
        # arrange
        MockPage.ClearMockResponse()
        mockPlaywright = MockPlaywright()
        helper = PlaywrightHelper()
        helper._playwright = mockPlaywright

        # act
        res = helper.FetchTargetApiByVisitingWebsite("dummy_url", "dummy_url")

        # assert
        self.assertTrue(res is None)

class FetchTargetApiByVisitingWebsite_IfHasResponse_ReturnTheResponse(BaseTestCase):
    def test(self):
        # arrange
        MockPage.ClearMockResponse()
        mockPlaywright = MockPlaywright()

        helper = PlaywrightHelper()
        helper._playwright = mockPlaywright

        mockRes = MockResponse(
            req=MockRequest(
                url="http://test.com/api",
            ),
            ok=True,
            json={"mock":"response"}
        )
        MockPage.AddMockResponse(mockRes)

        # act
        res = helper.FetchTargetApiByVisitingWebsite("http://test.com","http://test.com/api")

        # assert
        self.assertTrue(res["mock"] == "response")


class FetchTargetApiByVisitingWebsite_IfHasMultipleResponse_ResponseIsTheFirstResponseFetched(BaseTestCase):
    def test(self):
        # arrange
        MockPage.ClearMockResponse()
        mockPlaywright = MockPlaywright()

        helper = PlaywrightHelper()
        helper._playwright = mockPlaywright

        mockRes1 = MockResponse(
            req=MockRequest(
                url="http://test.com/api",
            ),
            ok=True,
            json={"mock":"response1"}
        )
        mockRes2 = MockResponse(
            req=MockRequest(
                url="http://test.com/api",
            ),
            ok=True,
            json={"mock":"response2"}
        )
        MockPage.AddMockResponse(mockRes1)
        MockPage.AddMockResponse(mockRes2)

        # act
        res = helper.FetchTargetApiByVisitingWebsite("http://test.com", "http://test.com/api")

        # assert
        self.assertTrue(res["mock"] == "response1")

class FetchTargetApiByVisitingWebsite_IfResNotOk_IgnoreResponse(BaseTestCase):
    def test(self):
        # arrange
        MockPage.ClearMockResponse()
        mockPlaywright = MockPlaywright()

        helper = PlaywrightHelper()
        helper._playwright = mockPlaywright

        mockRes = MockResponse(
            req=MockRequest(
                url="http://test.com/api",
            ),
            ok=False,
            json={"mock":"response"}
        )
        MockPage.AddMockResponse(mockRes)

        # act
        res = helper.FetchTargetApiByVisitingWebsite("http://test.com","http://test.com/api")

        # assert
        self.assertTrue(res is None)

class FetchTargetApiByVisitingWebsite_IfResIsNotXHR_Ignore(BaseTestCase):
    def test(self):
        # arrange
        MockPage.ClearMockResponse()
        mockPlaywright = MockPlaywright()

        helper = PlaywrightHelper()
        helper._playwright = mockPlaywright

        mockRes = MockResponse(
            req=MockRequest(
                url="http://test.com/api",
                resource_type="xml"
            ),
            ok=True,
            json={"mock":"response"}
        )
        MockPage.AddMockResponse(mockRes)

        # act
        res = helper.FetchTargetApiByVisitingWebsite("http://test.com","http://test.com/api")

        # assert
        self.assertTrue(res is None)
