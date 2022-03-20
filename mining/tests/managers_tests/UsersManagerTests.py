from mining.tests.BaseTestCase import BaseTestCase
from mining.managers.UsersManager import UsersManager
from mining.database.models.User import User

class QueryAllUsers_ShouldReturnAllUsers(BaseTestCase):
    def test(self):
        # arrange
        usersManager = UsersManager()

        # act
        all_users = usersManager.QueryAllUsers()

        # assert
        self.assertTrue(len(all_users) == 2)

class AddUser_IfUserIsValid_ThenUserShouldBeAdded(BaseTestCase):
    def test(self):
        # arrange
        usersManager = UsersManager()
        user = User(LIHKGUserId=200101, Nickname="new user", Gender="M", CreateDate=120000, LastUpdate=120000)

        # act
        usersManager.AddUser(user)
        res = usersManager.QueryUserByLIHKGUserId(200101)

        # assert
        self.assertTrue(res != None)

class AddUsers_IfUserIsInvalid_ExpectedException(BaseTestCase):
    def test(self):
        # arrange
        usersManager = UsersManager()
        user_without_nickname = User(LIHKGUserId=200101, Nickname=None, Gender="M", CreateDate=120000, LastUpdate=120000)

        # act
        self.assertRaises(Exception, usersManager.AddUser, user_without_nickname)
