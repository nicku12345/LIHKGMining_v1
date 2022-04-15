import json
from mining.tests.BaseTestCase import BaseTestCase


class GetLIHKGThreadsWorkQueue_WithAppSetUp_CanRetrieveQueue(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()

        # act
        res = client.get("/api/lihkgthreads/queue")

        # assert
        self.assertTrue(res.status_code == 200)
        self.assertTrue(res.json == []) # work queue is not activated

class ClearLIHKGThreadsWorkQueue_WithAppSetUp_CanClearQueue(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()

        # act
        res = client.post("/api/lihkgthreads/queue/clear")

        # assert
        self.assertTrue(res.status_code == 200)

class QueueFetchOneThreadPageByLIHKGThreadIdAndPage_WithAppSetUp_WorkQueued(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()
        body = json.dumps({"LIHKGThreadId": 1, "page": 1})

        # act
        res = client.post("/api/lihkgthreads/fetch/queue", data=body, content_type="application/json")

        # assert
        self.assertTrue(res.status_code == 200)

class QueueFetchOneThreadPageByLIHKGThreadIdAndPage_InvalidRequestBody_ThenExpectBadRequest(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()
        invalid_body1 = json.dumps({"lihkgthreadid": 1, "page": 1})     # letters are case-sensitive
        invalid_body2 = json.dumps({"LIHKGThreadId": "1", "page": 1})   # invalid data type
        invalid_body3 = json.dumps({"LIHKGThreadId": 1, "page": "1"})   # invalid data type

        # act
        res1 = client.post("/api/lihkgthreads/fetch/queue", data=invalid_body1, content_type="application/json")
        res2 = client.post("/api/lihkgthreads/fetch/queue", data=invalid_body2, content_type="application/json")
        res3 = client.post("/api/lihkgthreads/fetch/queue", data=invalid_body3, content_type="application/json")

        self.assertTrue(res1.status_code == 400)
        self.assertTrue(res2.status_code == 400)
        self.assertTrue(res3.status_code == 400)

class QueueFullFetchOneThreadByLIHKGThreadId_WithAppsetUp_WorkQueued(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()
        body = json.dumps({"LIHKGThreadId": 1})

        # act
        res = client.post("/api/lihkgthreads/fullfetch/queue", data=body, content_type="application/json")

        # assert
        self.assertTrue(res.status_code == 200)

class QueueFullFetchoneThreadByLIHKGThreadId_InvalidRequestBody_ThenExpectBadRequest(BaseTestCase):
    def test(self):

        client = self.GetTestClient()
        invalid_body1 = json.dumps({"lihkgthreadid": 1, "page": 1})     # letters are case-sensitive
        invalid_body2 = json.dumps({"LIHKGThreadId": "1", "page": 1})   # invalid data type
        invalid_body3 = json.dumps({"LIHKGThreadId": 1, "page": "1"})   # invalid data type

        # act
        res1 = client.post("/api/lihkgthreads/fullfetch/queue", data=invalid_body1, content_type="application/json")
        res2 = client.post("/api/lihkgthreads/fullfetch/queue", data=invalid_body2, content_type="application/json")
        res3 = client.post("/api/lihkgthreads/fullfetch/queue", data=invalid_body3, content_type="application/json")

        self.assertTrue(res1.status_code == 400)
        self.assertTrue(res2.status_code == 400)
        self.assertTrue(res3.status_code == 400)
