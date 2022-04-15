import json
from mining.tests.BaseTestCase import BaseTestCase


class QueryAllThreads_WithAppSetUp_ResponseStatusIs200(BaseTestCase):
    def test(self):
        # arrange
        client = self.GetTestClient()

        # act
        res = client.get("api/threads/query/all")

        # assert
        self.assertTrue(res.status_code == 200)
