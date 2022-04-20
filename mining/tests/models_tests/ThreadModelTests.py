from mining.tests.BaseTestCase import BaseTestCase
from mining.database.models.Thread import Thread
from datetime import datetime


class ThreadSerialize_Test(BaseTestCase):
    def test(self):
        # arrange
        thread = Thread(LIHKGThreadId=508, CategoryId=10, SubCategoryId=2, Title="test new thread", NumberOfReplies=1, NumberOfUniReplies=1, LikeCount=22, DislikeCount=0, CreateDate=82, LastUpdate=90)

        # act
        res = thread.Serialize()

        # assert
        self.assertTrue(isinstance(res, dict))
        self.assertTrue(res["LIHKGThreadId"] == 508)
        self.assertTrue(res["CategoryId"] == 10)
        self.assertTrue(res["SubCategoryId"] == 2)
        self.assertTrue(res["Title"] == "test new thread")
        self.assertTrue(res["NumberOfReplies"] == 1)
        self.assertTrue(res["NumberOfUniReplies"] == 1)
        self.assertTrue(res["LikeCount"] == 22)
        self.assertTrue(res["DislikeCount"] == 0)
        self.assertTrue(res["CreateDate"] == str(datetime.fromtimestamp(82)))
        self.assertTrue(res["LastUpdate"] == str(datetime.fromtimestamp(90)))
