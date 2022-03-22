from typing import Dict
from mining.database.models.User import User
from mining.database.models.Thread import Thread
from mining.database.models.Message import Message
from mining.managers.helpers.BaseHelper import BaseHelper


class LIHKGThreadsHelper(BaseHelper):

    def __init__(self):
        super().__init__()

    def GetFetchThreadWebsiteAndApiUrlPrefix(self, LIHKGThreadId: int, page: int):
        website_url = f"https://lihkg.com/thread/{LIHKGThreadId}/page/{page}"
        target_api_url_pref = f"https://lihkg.com/api_v2/thread/{LIHKGThreadId}/page/{page}"
        return website_url, target_api_url_pref

    def IsResponseSuccess(self, lihkg_thread: Dict):
        if lihkg_thread == None:
            return False

        return lihkg_thread.get("success") == 1

    def HasEmptyMessages(self, lihkg_thread: Dict):
        return len(lihkg_thread["response"]["item_data"]) == 0

    def ConvertToUser(self, lihkg_thread: Dict):
        user = User()

        user.LIHKGUserId    = int(lihkg_thread["response"]["user"]["user_id"])
        user.Nickname       = lihkg_thread["response"]["user"]["nickname"]
        user.Gender         = lihkg_thread["response"]["user"]["gender"]
        user.CreateDate     = int(lihkg_thread["response"]["user"]["create_time"])
        user.LastUpdate     = int(lihkg_thread["response"]["user"]["create_time"])

        return user

    def ConvertToMessages(self, lihkg_thread: Dict):
        messages = list()
        for lihkg_msg in lihkg_thread["response"]["item_data"]:
            msg = Message()

            msg.MessageNumber   = int(lihkg_msg["msg_num"])
            msg.Message         = lihkg_msg["msg"]
            msg.LikeCount       = int(lihkg_msg["like_count"])
            msg.DislikeCount    = int(lihkg_msg["dislike_count"])
            msg.CreateDate      = int(lihkg_msg["reply_time"])
            msg.LastUpdate      = int(lihkg_msg["reply_time"])

            messages.append(msg)

        return messages

    def ConvertToUsers(self, lihkg_thread: Dict):
        users = list()
        for lihkg_msg in lihkg_thread["response"]["item_data"]:
            user = User()

            user.LIHKGUserId    = int(lihkg_msg["user"]["user_id"])
            user.Nickname       = lihkg_msg["user"]["nickname"]
            user.Gender         = lihkg_msg["user"]["gender"]
            user.CreateDate     = int(lihkg_msg["user"]["create_time"])
            user.LastUpdate     = int(lihkg_msg["user"]["create_time"])

            users.append(user)

        return users

    def ConvertToThread(self, lihkg_thread: Dict):
        thread = Thread()

        thread.LIHKGThreadId       = int(lihkg_thread["response"]["thread_id"])
        thread.CategoryId          = int(lihkg_thread["response"]["cat_id"])
        thread.SubCategoryId       = int(lihkg_thread["response"]["sub_cat_id"])
        thread.Title               = lihkg_thread["response"]["title"]
        thread.NumberOfReplies     = int(lihkg_thread["response"]["no_of_reply"])
        thread.NumberOfUniReplies  = int(lihkg_thread["response"]["no_of_uni_user_reply"])
        thread.LikeCount           = int(lihkg_thread["response"]["like_count"])
        thread.DislikeCount        = int(lihkg_thread["response"]["dislike_count"])
        thread.CreateDate          = int(lihkg_thread["response"]["create_time"])
        thread.LastUpdate          = int(lihkg_thread["response"]["last_reply_time"])

        return thread



