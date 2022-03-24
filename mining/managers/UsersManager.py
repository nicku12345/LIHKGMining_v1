"""
Concrete manager for user related functionalities.
"""
from typing import List
from mining.database.models.User import User
from mining.database.repositories.UsersRepository import UsersRepository
from mining.managers.BaseManager import BaseManager
from mining.util.Exceptions import *

class UsersManager(BaseManager):
    """
    Concrete manager for user related functionalities.
    """

    def __init__(self):
        super().__init__()
        self._usersRepo = UsersRepository()

    def QueryAllUsers(self):
        '''
        Query all users.
        '''
        return self._usersRepo.QueryAllUsers()

    def QueryUserByLIHKGUserId(self, LIHKGUserId: int):
        '''
        Query user by LIHKGUserId.

        Returns user if found, None otherwise.
        '''
        return self._usersRepo.QueryUserByLIHKGUserId(LIHKGUserId=LIHKGUserId)

    def QueryUsersByLIHKGUserIds(self, LIHKGUserIds: List[int]):
        '''
        Query users by a list of LIHKGUserIds.

        Returns a dictionary of storing (LIHKGUserId, user) key value pair.
        '''
        return self._usersRepo.QueryUsersByLIHKGUserIds(LIHKGUserIds=LIHKGUserIds)

    def AddUser(self, user: User):
        '''
        Adds a user to the database.
        '''
        self._logger.info("Adding user...")
        self._logger.debug(user)
        try:
            self._usersRepo.AddUser(user)
        except Exception as e:
            err_msg = f"Failed to add user. Error: {e}"
            self._logger.error(err_msg)
            raise BadRequest(err_msg) from e
        else:
            self._logger.info(f"User {user} added!")
