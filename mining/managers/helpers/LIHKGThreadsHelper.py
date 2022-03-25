"""
Concrete helper class for LIHKG threads related functionalities.
"""
from typing import Dict

from mining.database.models.User import User
from mining.database.models.Thread import Thread
from mining.database.models.Message import Message
from mining.managers.helpers.BaseHelper import BaseHelper
from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob


class LIHKGThreadsHelper(BaseHelper):
    """
    Concrete helper class for LIHKG threads related functionalities.
    """

    def GetFetchThreadWebsiteAndApiUrlPrefix(self, LIHKGThreadId: int, page: int):
        '''
        Returns the website url and target api to fetch for
        a given LIHKG thread id and page number.
        '''
        website_url = f"https://lihkg.com/thread/{LIHKGThreadId}/page/{page}"
        target_api_url_pref = f"https://lihkg.com/api_v2/thread/{LIHKGThreadId}/page/{page}"
        return website_url, target_api_url_pref

    def GetLIHKGThreadJobWebsiteAndApiUrlPrefix(self, category: int = 1):
        '''
        Returns the website url and target api to fetch for
        a given category.

        The default category is 1, which contains threads of all
        other categories.
        '''
        website_url = f"https://lihkg.com/category/{category}"
        target_api_url_pref = f"https://lihkg.com/api_v2/thread/latest?cat_id={category}"
        return website_url, target_api_url_pref

    def IsResponseSuccess(self, lihkg_thread: Dict):
        '''
        Checks whether the fetched data contains success in its response
        '''
        if lihkg_thread is None:
            return False

        return lihkg_thread.get("success") == 1

    def HasEmptyMessages(self, lihkg_thread: Dict):
        '''
        Checks whether the fetched thread page contains any messages.

        Used to determine whether the page is the last page.
        '''
        return len(lihkg_thread["response"]["item_data"]) == 0

    def ConvertToUser(self, lihkg_thread: Dict):
        '''
        Converts the fetched response to user,
        the author of the thread.
        '''
        user = User()

        user.LIHKGUserId    = int(lihkg_thread["response"]["user"]["user_id"])
        user.Nickname       = lihkg_thread["response"]["user"]["nickname"]
        user.Gender         = lihkg_thread["response"]["user"]["gender"]
        user.CreateDate     = int(lihkg_thread["response"]["user"]["create_time"])
        user.LastUpdate     = int(lihkg_thread["response"]["user"]["create_time"])

        return user

    def ConvertToMessages(self, lihkg_thread: Dict):
        '''
        Converts the fetched response to a list of messages.
        '''
        messages = []
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
        '''
        Converts the fetched response to a list of users matching the messages.
        '''
        users = []
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
        '''
        Converts the fetched response to a thread.
        '''
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

    def ConvertToJobs(self, lihkg_category_response: Dict):
        '''
        Converts the fetched response to a list of LIHKGThreadJobs.
        '''
        jobs = []

        for thread in lihkg_category_response["response"]["items"]:
            LIHKGThreadId = thread["thread_id"]
            job = LIHKGThreadsJob(
                LIHKGThreadId=LIHKGThreadId,
                page=1,
                isFullFetch=True
            )

            jobs.append(job)

        return jobs
