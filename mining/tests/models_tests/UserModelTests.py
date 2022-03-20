from mining.tests.BaseTestCase import BaseTestCase
from mining.database.repositories.UsersRepository import UsersRepository
from mining.database.models.User import User
import datetime

class UserRepr_IfContainsNonEnglishCharacters_CanDisplayProperly(BaseTestCase):
    def test(self):
        # arrange
        user = User(LIHKGUserId=10, Nickname="*#@$& 中文字 plus some English", Gender="M", CreateDate=12, LastUpdate=12)

        # act
        representation = user.__repr__()

        # assert
        expected_representation = "<User(LIHKGUserId=10, Nickname=*#@$& 中文字 plus some English, Gender=M, CreateDate=12, LastUpdate=12, RetrievedDate=None)>"
        self.assertTrue(representation == expected_representation)

class UserUpdate_IfOriginalUserIsLatter_NoNeedToUpdate(BaseTestCase):
    def test(self):
        # arrange
        current_user = User(LIHKGUserId=98, Nickname="user", Gender="M", CreateDate=12, LastUpdate=12)
        outdated_user = User(LIHKGUserId=90, Nickname="outdated user", Gender="F", CreateDate=12, LastUpdate=8)

        # act
        current_user.Update(outdated_user)

        # assert
        self.assertTrue(current_user.LIHKGUserId == 98)
        self.assertTrue(current_user.Nickname == "user")
        self.assertTrue(current_user.Gender == "M")
        self.assertTrue(current_user.CreateDate == 12)
        self.assertTrue(current_user.LastUpdate == 12)


class UserUpdate_IfOriginalUserIsOutdated_Update(BaseTestCase):
    def test(self):
        # arrange
        current_user = User(LIHKGUserId=98, Nickname="user", Gender="M", CreateDate=12, LastUpdate=12)
        updated_user = User(LIHKGUserId=90, Nickname="updated user", Gender="F", CreateDate=4, LastUpdate=35)

        # act
        current_user.Update(updated_user)

        # assert
        self.assertTrue(current_user.LIHKGUserId == 90)
        self.assertTrue(current_user.Nickname == "updated user")
        self.assertTrue(current_user.Gender == "F")
        self.assertTrue(current_user.CreateDate == 4)
        self.assertTrue(current_user.LastUpdate == 35)
