import json
from mining.tests.BaseTestCase import BaseTestCase
from mining.managers.helpers.LIHKGThreadsHelper import LIHKGThreadsHelper
from mining.database.models.User import User
from mining.database.models.Thread import Thread
from mining.database.models.Message import Message
from mining.tests._mock_data.examples.lihkg_api_v2_thread_example import example_json_response

class LIHKGThreadsHelperTestCase(BaseTestCase):

    _example_json_response = example_json_response

    @classmethod
    def GetExampleJson(cls):
        return example_json_response

class IsResponseSuccess_IfInputIsSuccess_ShouldReturnTrue(LIHKGThreadsHelperTestCase):
    def test(self):
        # arrange
        example_json = self.GetExampleJson()
        helper = LIHKGThreadsHelper()

        # act
        res = helper.IsResponseSuccess(example_json)

        # assert
        self.assertTrue(res)

class IsResponseSuccess_IfInputIsNone_ShouldReturnFalse(LIHKGThreadsHelperTestCase):
    def test(self):
        # arrange
        helper = LIHKGThreadsHelper()

        # act
        res = helper.IsResponseSuccess(None)

        # assert
        self.assertFalse(res)

class HasEmptyMessages_IfHasMessages_ReturnFalse(LIHKGThreadsHelperTestCase):
    def test(self):
        # arrange
        example_json = self.GetExampleJson()
        helper = LIHKGThreadsHelper()

        # act
        res = helper.HasEmptyMessages(example_json)

        # assert
        self.assertFalse(res)

class ConvertToUser_IfResponseIsSuccess_ReturnUser(LIHKGThreadsHelperTestCase):
    def test(self):
        # arrange
        example_json = self.GetExampleJson()
        helper = LIHKGThreadsHelper()

        # act
        user = helper.ConvertToUser(example_json)

        # assert
        self.assertTrue(user.LIHKGUserId == 31374)

class ConvertToThread_IfResponseIsSuccess_ReturnThread(LIHKGThreadsHelperTestCase):
    def test(self):
        # arrange
        example_json = self.GetExampleJson()
        helper = LIHKGThreadsHelper()

        # act
        thread = helper.ConvertToThread(example_json)

        # assert
        self.assertTrue(thread.LIHKGThreadId == 2651271)

class ConvertToMessagesAndConvertToUsers_IfResponseIsSuccess_SizesShouldBeSame(LIHKGThreadsHelperTestCase):
    def test(self):
        # arrange
        example_json = self.GetExampleJson()
        helper = LIHKGThreadsHelper()

        # act
        messages = helper.ConvertToMessages(example_json)
        users = helper.ConvertToUsers(example_json)

        # assert
        self.assertTrue(len(messages) == len(users))
