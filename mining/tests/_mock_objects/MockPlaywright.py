
class MockPlaywright:
    def __init__(self):
        self.webkit = MockWebkit()

    def stop(self):
        return

class MockWebkit:
    def launch(self):
        return MockBrowser()

class MockBrowser:
    def new_page(self):
        return MockPage()

    def close(self):
        return

class MockPage:

    _mock_res = []

    def __init__(self):
        self._f = None

    def on(self, event_type, f):
        self._f = f
        pass

    def goto(self, website_url, timeout=0, wait_until="networkidle"):
        for res in self._mock_res:
            self._f(res)

    @classmethod
    def AddMockResponse(cls, res):
        cls._mock_res.append(res)

    @classmethod
    def ClearMockResponse(cls):
        cls._mock_res = []

class MockRequest:
    def __init__(self, url="", resource_type="xhr"):
        self.url = url
        self.resource_type = resource_type

class MockResponse:
    def __init__(self, req=MockRequest(), ok=True, json={}):
        self.request = req
        self.ok = ok
        self._json = json

    def json(self):
        return self._json
