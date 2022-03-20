from mining.tests.BaseTestCase import BaseTestCase
from mining.database.repositories.UsersRepository import UsersRepository
from mining.database.models.User import User


class QueryAllUsers_ShouldReturnAllUsers(BaseTestCase):
    def test(self):
        # arrange
        usersRepo = UsersRepository()

        # act
        all_users = usersRepo.QueryAllUsers()

        # assert
        self.assertTrue(len(all_users) == 2)        # Number of mock users

class AddUser_IfNicknameContainsNonEnglishChars_CanBeSavedProperly(BaseTestCase):
    def test(self):
        # arrange
        usersRepo = UsersRepository()
        user = User(LIHKGUserId=200101, Nickname="*#@$& 中文字 plus some English", Gender="M", CreateDate=120000, LastUpdate=120000)

        # act
        usersRepo.AddUser(user)
        res = usersRepo.QueryUserByLIHKGUserId(200101)

        # assert
        self.assertTrue(res != None)
        self.assertTrue(res.Nickname == "*#@$& 中文字 plus some English")

class AddUser_IfLIHKGUserIdAlreadyExists_ThenExpectException(BaseTestCase):
    def test(self):
        # arrange
        usersRepo = UsersRepository()
        user = User(LIHKGUserId=1, Nickname="700001 already exists in mock users", Gender="M", CreateDate=120000, LastUpdate=120000)

        # act
        self.assertRaises(Exception, usersRepo.AddUser, user)

class AddUser_IfUserIsOkToAdd_ThenAddedToDatabase(BaseTestCase):
    def test(self):
        # arrange
        usersRepo = UsersRepository()
        user = User(LIHKGUserId=200101, Nickname="new user", Gender="M", CreateDate=120000, LastUpdate=120000)
        all_users = usersRepo.QueryAllUsers()

        # act
        usersRepo.AddUser(user)
        new_all_users = usersRepo.QueryAllUsers()

        # assert
        self.assertTrue(len(all_users) + 1 == len(new_all_users))

class QueryUserByLIHKGUserId_IfLIHKGUserIdExistsInDB_ThenReturnThatUser(BaseTestCase):
    def test(self):
        # arrange
        usersRepo = UsersRepository()
        user = User(LIHKGUserId=200101, Nickname="new user", Gender="M", CreateDate=120000, LastUpdate=120000)
        usersRepo.AddUser(user)

        # act
        res = usersRepo.QueryUserByLIHKGUserId(200101)

        # assert
        self.assertTrue(res != None)
        self.assertTrue(res.LIHKGUserId == 200101)
        self.assertTrue(res.Nickname == "new user")
        self.assertTrue(res.Gender == "M")
        self.assertTrue(res.CreateDate == 120000)
        self.assertTrue(res.LastUpdate == 120000)

class QueryUserByLIHKGUserId_IfLIHKGUserIdDoesNotExist_ThenReturnNone(BaseTestCase):
    def test(self):
        # arrange
        usersRepo = UsersRepository()

        # act
        res = usersRepo.QueryUserByLIHKGUserId(LIHKGUserId=40499999)

        # assert
        self.assertTrue(res == None)

class MergeAndSaveUser_IfMerged_ThenChangesAreApplied(BaseTestCase):
    def test(self):
        # arrange
        user = User(LIHKGUserId=200101, Nickname="test user", Gender="M", CreateDate=120000, LastUpdate=120000)
        usersRepo = UsersRepository()
        usersRepo.AddUser(user)

        updated_user = User(LIHKGUserId=200102, Nickname="updated test user", Gender="F", CreateDate=300000, LastUpdate=300001)
        updated_user.UserId = user.UserId

        # act
        usersRepo.MergeUser(updated_user)
        res = usersRepo.QueryUserByLIHKGUserId(200102)

        # assert
        self.assertTrue(res != None)
        self.assertTrue(res == user)                # queried user and user have the same instance
        self.assertTrue(updated_user != user)       # updated_user and user are two different instances

        self.assertTrue(user.LIHKGUserId == 200102)
        self.assertTrue(user.Nickname == "updated test user")
        self.assertTrue(user.Gender == "F")
        self.assertTrue(user.CreateDate == 300000)
        self.assertTrue(user.LastUpdate == 300001)