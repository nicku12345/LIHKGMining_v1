from mining.tests.BaseTestCase import BaseTestCase
from mining.database.models.Message import Message


class ModelSerialize_Test(BaseTestCase):
    def test(self):
        # arrange
        msg = Message(LikeCount=6, DislikeCount=10, Message="test message", MessageNumber=0, CreateDate=82, LastUpdate=90)

        # act
        res = msg.Serialize()

        # assert
        self.assertTrue(isinstance(res, dict))
        self.assertTrue(res["LikeCount"] == 6)
        self.assertTrue(res["DislikeCount"] == 10)
        self.assertTrue(res["Message"] == "test message")
        self.assertTrue(res["MessageNumber"] == 0)
        self.assertTrue(res["CreateDate"] == 82)
        self.assertTrue(res["LastUpdate"] == 90)
