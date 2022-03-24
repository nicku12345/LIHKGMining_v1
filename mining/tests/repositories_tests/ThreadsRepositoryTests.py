from mining.tests.BaseTestCase import BaseTestCase
from mining.database.models.Thread import Thread
from mining.database.models.User import User
from mining.database.models.Message import Message
from mining.database.repositories.ThreadsRepository import ThreadsRepository

class QueryAllThreads_ShouldReturnAllThreads(BaseTestCase):
    def test(self):
        # arrange
        threadsRepo = ThreadsRepository()

        # act
        all_threads = threadsRepo.QueryAllThreads()

        # assert
        self.assertTrue(len(all_threads) == 1)
        self.assertTrue(all_threads[0].Title == "test thread 1")
        self.assertTrue(len(all_threads[0].Messages) == 2)

class AddThread_IfThreadIsOkToAdd_ThenThreadIsAdded(BaseTestCase):
    def test(self):
        # arrange
        thread = Thread(LIHKGThreadId=508, CategoryId=10, SubCategoryId=2, Title="test thread", NumberOfReplies=1,
                        NumberOfUniReplies=1, LikeCount=22, DislikeCount=0, CreateDate=82, LastUpdate=90)
        user = User(LIHKGUserId=508001, Nickname="test thread author", Gender="M", CreateDate=120000, LastUpdate=120000)
        message = Message(LikeCount=0, DislikeCount=0, Message="test message", MessageNumber=0, CreateDate=82, LastUpdate=90)

        thread.User = user
        message.User = user
        thread.Messages.append(message)

        # act
        threadsRepo = ThreadsRepository()
        threadsRepo.AddThread(thread)
        res = threadsRepo.QueryThreadByLIHKGThreadId(508)

        # assert
        self.assertTrue(res != None)
        self.assertTrue(res.CategoryId == 10)
        self.assertTrue(res.SubCategoryId == 2)
        self.assertTrue(res.Title == "test thread")
        self.assertTrue(res.NumberOfReplies == 1)
        self.assertTrue(res.NumberOfUniReplies == 1)
        self.assertTrue(res.LikeCount == 22)
        self.assertTrue(res.DislikeCount == 0)
        self.assertTrue(res.CreateDate == 82)
        self.assertTrue(res.LastUpdate == 90)
        self.assertTrue(res.User.LIHKGUserId == 508001)
        self.assertTrue(len(res.Messages) == 1)
        self.assertTrue(res.Messages[0].Message == "test message")
        self.assertTrue(res.Messages[0].User.LIHKGUserId == 508001)

class AddThread_IfThreadAlreadyExists_RaiseException(BaseTestCase):
    def test(self):
        # arrange
        thread = Thread(LIHKGThreadId=1, CategoryId=10, SubCategoryId=2, Title="test duplicate thread", NumberOfReplies=1,
                        NumberOfUniReplies=1, LikeCount=22, DislikeCount=0, CreateDate=82, LastUpdate=90)

        # act
        threadsRepo = ThreadsRepository()
        self.assertRaises(Exception, threadsRepo.AddThread, thread)
