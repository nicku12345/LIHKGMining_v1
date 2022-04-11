"""
Concrete manager class for thread entities related functionalities.
"""
from typing import List
from mining.managers.BaseManager import BaseManager
from mining.managers.UsersManager import UsersManager
from mining.database.repositories.ThreadsRepository import ThreadsRepository
from mining.database.models.User import User
from mining.database.models.Message import Message
from mining.database.models.Thread import Thread
from mining.util.Exceptions import BadRequest


class ThreadsManager(BaseManager):
    """
    Concrete manager class for thread entities related functionalities.
    """

    def __init__(self):
        super().__init__()
        self._threadsRepo = ThreadsRepository()
        self._usersManager = UsersManager()

    def QueryAllThreads(self, skip_messages=False):
        '''
        Returns a list of all threads in the attached Threads table.
        '''
        return self._threadsRepo.QueryAllThreads(skip_messages=skip_messages)

    def QueryThreadByLIHKGThreadId(self, LIHKGThreadId):
        '''
        Returns the thread having the LIHKGThreadId provided.

        Returns None otherwise.
        '''
        return self._threadsRepo.QueryThreadByLIHKGThreadId(LIHKGThreadId=LIHKGThreadId)

    def AddThread(self, thread: Thread, user: User, messages: List[Message], users: List[User]):
        '''
        Add the thread to the database.
        If a thread with the same LIHKGThreadId already exists,
        it will update the thread, relevant messages and relevant users if necessary.

        :param thread: The thread with attributes filled.
        :param user: The associated user of the thread.
        :param messages: A list of messages found for this thread. Messages and users must have the same size
        :param users: A list of associated users for the messages. Messages and users must have the same size
        '''
        self._logger.info("Received add thread request.")
        self._logger.debug(f"Thread={thread}")
        self._logger.debug(f"User={user}")
        self._logger.debug(f"Number of messages={len(messages)}")

        if thread.LIHKGThreadId is None:
            raise BadRequest(f"Thread does not have LIHKGThreadId. Thread={thread}")

        if user.LIHKGUserId is None:
            raise BadRequest(f"User does not have LIHKGUserId. User={user}")

        if len(messages) != len(users):
            raise BadRequest(f"Length of messages ({len(messages)}) does not equal length of users ({len(users)})")

        '''
        Pre-process: replace user and users by existing entities and remove potential duplicate instances for the same user
        '''
        existing_user = self._usersManager.QueryUserByLIHKGUserId(user.LIHKGUserId)
        if existing_user is None:
            self._logger.info("Author of the thread is a new user.")
            self._usersManager.AddUser(user)
        else:
            self._logger.info("Author of the thread is an existing user.")
            existing_user.Update(user)
            user = existing_user

        users = self._UpdateOrEliminateDuplicateUserInstances(users)

        existing_thread = self.QueryThreadByLIHKGThreadId(LIHKGThreadId=thread.LIHKGThreadId)
        if existing_thread is None:
            self._logger.info(f"No existing matching thread for {thread.LIHKGThreadId} found. Creating one new thread...")
            self._CreateNewThread(thread, user, messages, users)
        else:
            self._logger.info(f"LIHKGThreadId: {thread.LIHKGThreadId} exists. Updating the thread...")
            self._UpdateExistingThread(existing_thread, thread, user, messages, users)

    def _UpdateOrEliminateDuplicateUserInstances(self, users: List[User]):
        '''
        Ensure that one LIHKGUserId has only one user instance.
        '''

        # At this stage, author of the thread must be an existing user.
        # Therefore, user must be inside this dictionary.
        LIHKGUserId_User_Map = self._usersManager.QueryUsersByLIHKGUserIds([u.LIHKGUserId for u in users])

        for i,u in enumerate(users):
            u_LIHKGUserId = u.LIHKGUserId
            if u_LIHKGUserId in LIHKGUserId_User_Map:
                LIHKGUserId_User_Map[u_LIHKGUserId].Update(u)
                users[i] = LIHKGUserId_User_Map[u_LIHKGUserId]
            else:
                LIHKGUserId_User_Map[u_LIHKGUserId] = u

        return users

    def _CreateNewThread(self, thread: Thread, user: User, messages: List[Message], users: List[User]):
        thread.User = user
        for msg,u in zip(messages,users):
            msg.User = u

            thread.Messages.append(msg)

        self._threadsRepo.AddThread(thread)

    def _UpdateExistingThread(self, existing_thread: Thread, thread: Thread, user: User, messages: List[Message], users: List[User]):
        existing_thread.Update(thread)

        existing_messages = {msg.MessageNumber: msg for msg in existing_thread.Messages}

        for msg,u in zip(messages,users):
            if msg.MessageNumber in existing_messages:
                existing_msg = existing_messages[msg.MessageNumber]
                existing_msg.Update(msg)
            else:
                msg.User = u

                existing_thread.Messages.append(msg)

        self._threadsRepo.MergeThread(existing_thread)
