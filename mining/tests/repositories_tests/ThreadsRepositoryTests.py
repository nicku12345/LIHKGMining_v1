from mining.tests.BaseTestCase import BaseTestCase
from mining.database.models.Thread import Thread
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