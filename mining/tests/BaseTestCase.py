from typing import Any, List
from flask_testing import TestCase
from mining.app import LIHKGMiningApp
from mining.database import db
from mining.database.models.Thread import Thread
from mining.database.models.User import User
from mining.database.models.Message import Message
from mining.tests._mock_data.UsersMockData import mock_users
from mining.tests._mock_data.MessagesMockData import mock_messages
from mining.tests._mock_data.ThreadsMockData import mock_threads


class BaseTestCase(TestCase):
    '''
    Base class of a test case.

    It handles:
        (1) instantiating the flask app in test environment,
        (2) database clean-ups and set-ups before and after test case run

    Usage: For each test case, subclass this base class using the following pattern:

    class MethodName_IfConditionHolds_ThenAssertExpectedResult(BaseTestCase):
        def test():
            # arrange
            ...

            # act
            ...

            # assert
            ...
    '''

    _mock_users = mock_users
    _mock_messages = mock_messages
    _mock_threads = mock_threads

    def __init__(self, *args, **kwargs):
        # allow args and kwargs from the unittest module to be provided properly
        super().__init__(*args, **kwargs)
        self._db = db
        self._app = self.create_app()

    def create_app(self):
        return LIHKGMiningApp.CreateApp(ENV="TEST")

    def setUp(self):
        self.cleanDatabase()
        # create the tables after we clean up the old data
        self._db.init_app(self._app)
        self.setUpDatabase()

    def tearDown(self):
        self._db.session.remove()
        self.cleanDatabase()

    def cleanDatabase(self):
        '''
        Remove every row found in the test database.

        This function is called every time before and after a test case.

        If the database uri does not point to a test database, error will be thrown.
        '''
        # safety check: do not delete database which is not a test database
        database_uri = self._app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_uri.endswith("test.db"):
            raise (f"Database {database_uri} is not a test database!")

        from mining.database.models.User import User
        from mining.database.models.Thread import Thread
        from mining.database.models.Message import Message

        self._db.session.query(User).delete()
        self._db.session.query(Thread).delete()
        self._db.session.query(Message).delete()
        self._db.session.commit()

    def setUpDatabase(self):
        '''
        Sets up the mock data

        The scope of the mock data is per test case.

        This means that each test case will share the same set of mock data created in here.
        '''

        self.AddMockUsers()
        self.AddMockThreadsWithMockMessages()

    def AddMockUsers(self):
        '''
        Utility function for adding a list of mock users to the database.
        '''
        for u in self._mock_users:
            '''
            Pass u.Copy() to the session to prevent the user from being attached to previous session
            u must have a working copy method
            '''
            self._db.session.add(u.Copy())
        self._db.session.commit()

    def AddMockThreadsWithMockMessages(self):
        '''
        Utility function for adding a list of mock threads associated with mock messages to database.

        We expect it is sufficient by providing foreign keys in the mock data, without linking to corresponding entities.
        However, manipulating foreign keys directly is not recommended for sqlalchemy.
        Therefore, it is quite difficult to create relations by foreign keys only.

        see https://stackoverflow.com/questions/66061526/not-null-constraint-failed-when-persisting-orm-object
        '''
        threadIdsMap = dict()
        for thread in self._mock_threads:
            '''
            Create a copy of the mock thread to prevent the thread from being attached to previous session
            
            Save the User_UserId here because Thread.Copy method does not manipulate foreign keys
            '''
            user_userId = thread.User_UserId
            thread = thread.Copy()

            thread.User = self._db.session.query(User).filter_by(UserId = user_userId).first()
            threadIdsMap[thread.ThreadId] = thread

        for msg in self._mock_messages:
            '''
            Create a copy of the mock message to prevent the message from being attached to previous session
            
            Save the User_UserId here because Message.Copy method does not manipulate foreign keys
            '''
            user_userId = msg.User_UserId
            msg = msg.Copy()

            msg.User = self._db.session.query(User).filter_by(UserId = user_userId).first()
            threadIdsMap[msg.Thread_ThreadId].Messages.append(msg)

        for threadId in threadIdsMap:
            # add the mock thread copies with mock messages attached to the database
            self._db.session.add(threadIdsMap[threadId])

        self._db.session.commit()