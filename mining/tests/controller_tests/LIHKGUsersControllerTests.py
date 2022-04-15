import json
from mining.tests.BaseTestCase import BaseTestCase


class QueryAllMessagesByLIHKGUserId_WithAppSetUp_ResponseStatusIs200(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()
        body = json.dumps({"LIHKGUserId": 31374})

        # act
        res = client.post("/api/lihkgusers/messages/query/all", data=body, content_type="application/json")

        # assert
        self.assertTrue(res.status_code == 200)

class QueryAllMessagesByLIHKGUserId_InvalidRequestBody_ThenExpectBadRequest(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()
        invalid_body1 = {"lihkguserid": 31374}           # request body is case sensitive
        invalid_body2 = {"LIHKGUserId": "31374"}         # invalid data type

        # act
        res1 = client.post("/api/lihkgusers/messages/query/all", data=invalid_body1, content_type="application/json")
        res2 = client.post("/api/lihkgusers/messages/query/all", data=invalid_body2, content_type="application/json")

        # assert
        self.assertTrue(res1.status_code == 400)
        self.assertTrue(res2.status_code == 400)

