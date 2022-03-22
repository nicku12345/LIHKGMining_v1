from mining.tests.BaseTestCase import BaseTestCase
from mining.managers.ThreadsManager import ThreadsManager
from mining.database.models.Thread import Thread
from mining.database.models.User import User
from mining.database.models.Message import Message

class AddThread_IfThreadDoesNotExistButUserExists_ThenThreadIsCreatedAndUsersAreUpdatedIfNecessary(BaseTestCase):
    def test(self):
        # assert
        thread = Thread(LIHKGThreadId=508, CategoryId=10, SubCategoryId=2, Title="test new thread", NumberOfReplies=1, NumberOfUniReplies=1, LikeCount=22, DislikeCount=0, CreateDate=82, LastUpdate=90)
        msgs = [Message(LikeCount=0, DislikeCount=0, Message="test message", MessageNumber=0, CreateDate=82, LastUpdate=90)]
        user = User(LIHKGUserId=1, Nickname="test member 1 updated", Gender="M", CreateDate=120000, LastUpdate=3000000)
        users = [User(LIHKGUserId=1, Nickname="test member 1", Gender="M", CreateDate=120000, LastUpdate=120000)]

        # act
        threadsManager = ThreadsManager()
        threadsManager.AddThread(thread, user, msgs, users)
        res = threadsManager.QueryThreadByLIHKGThreadId(508)

        # assert
        self.assertTrue(res != None)
        self.assertTrue(res.Title == "test new thread")
        self.assertTrue(res.User.LIHKGUserId == 1)
        self.assertTrue(res.User.Nickname == "test member 1 updated")
        self.assertTrue(res.User.LastUpdate == 3000000)
        self.assertTrue(res.User.RetrievedDate != None)
        self.assertTrue(len(res.Messages) == 1)
        self.assertTrue(res.Messages[0].User.LIHKGUserId == 1)
        self.assertTrue(res.Messages[0].User.Nickname == "test member 1 updated")
        self.assertTrue(res.Messages[0].User.LastUpdate == 3000000)
        self.assertTrue(res.Messages[0].User.RetrievedDate != None)

class AddThread_MethodIsIdempotent(BaseTestCase):
    def test(self):
        # assert
        thread = Thread(LIHKGThreadId=1, CategoryId=10, SubCategoryId=2, Title="test new thread", NumberOfReplies=1, NumberOfUniReplies=1, LikeCount=22, DislikeCount=0, CreateDate=82, LastUpdate=90)
        user = User(LIHKGUserId=11, Nickname="test member 1 updated", Gender="M", CreateDate=120000, LastUpdate=3000000)
        msgs = [
            Message(LikeCount=0, DislikeCount=0, Message="test message", MessageNumber=3, CreateDate=82, LastUpdate=90),
            Message(LikeCount=6, DislikeCount=3, Message="test reply~~", MessageNumber=4, CreateDate=87, LastUpdate=99)
        ]
        users = [
            User(LIHKGUserId=11, Nickname="test member 1", Gender="M", CreateDate=120000, LastUpdate=120000),
            User(LIHKGUserId=51, Nickname="test member 5", Gender="F", CreateDate=160900, LastUpdate=300000)
        ]

        # act
        threadsManager = ThreadsManager()
        threadsManager.AddThread(thread.Copy(), user.Copy(), [msg.Copy() for msg in msgs], [u.Copy() for u in users])
        threadsManager.AddThread(thread.Copy(), user.Copy(), [msg.Copy() for msg in msgs], [u.Copy() for u in users])
        threadsManager.AddThread(thread.Copy(), user.Copy(), [msg.Copy() for msg in msgs], [u.Copy() for u in users])
        res = threadsManager.QueryThreadByLIHKGThreadId(1)

        # assert
        self.assertTrue(res != None)
        self.assertTrue(res.Title == "test new thread")

        self.assertTrue(res.User.LIHKGUserId == 11)
        self.assertTrue(res.User.Nickname == "test member 1 updated")
        self.assertTrue(res.User.LastUpdate == 3000000)
        self.assertTrue(res.User.RetrievedDate != None)
        self.assertTrue(len(res.Messages) == 2)

        self.assertTrue(res.Messages[0].Message == "test message")
        self.assertTrue(res.Messages[0].MessageNumber == 3)
        self.assertTrue(res.Messages[0].User.LIHKGUserId == 11)
        self.assertTrue(res.Messages[0].User.Nickname == "test member 1 updated")
        self.assertTrue(res.Messages[0].User.Gender == "M")
        self.assertTrue(res.Messages[0].User.CreateDate == 120000)
        self.assertTrue(res.Messages[0].User.LastUpdate == 3000000)
        self.assertTrue(res.Messages[0].User.RetrievedDate != None)

        self.assertTrue(res.Messages[1].Message == "test reply~~")
        self.assertTrue(res.Messages[1].MessageNumber == 4)
        self.assertTrue(res.Messages[1].User.LIHKGUserId == 51)
        self.assertTrue(res.Messages[1].User.Nickname == "test member 5")
        self.assertTrue(res.Messages[1].User.Gender == "F")
        self.assertTrue(res.Messages[1].User.CreateDate == 160900)
        self.assertTrue(res.Messages[1].User.LastUpdate == 300000)
        self.assertTrue(res.Messages[1].User.RetrievedDate != None)