from typing import List
from mining.database.models.User import User
from mining.database.repositories.UsersRepository import UsersRepository
from mining.managers.BaseManager import BaseManager
from mining.util.Exceptions import *

class UsersManager(BaseManager):

    def __init__(self):
        super().__init__()
        self._usersRepo = UsersRepository()

    def QueryAllUsers(self):
        return self._usersRepo.QueryAllUsers()

    def QueryUserByLIHKGUserId(self, LIHKGUserId: int):
        return self._usersRepo.QueryUserByLIHKGUserId(LIHKGUserId=LIHKGUserId)

    def QueryUsersByLIHKGUserIds(self, LIHKGUserIds: List[int]):
        return self._usersRepo.QueryUsersByLIHKGUserIds(LIHKGUserIds=LIHKGUserIds)

    def AddUser(self, user: User):
        self._logger.info(f"Adding user...")
        self._logger.debug(user)
        try:
            self._usersRepo.AddUser(user)
        except Exception as e:
            err_msg = f"Failed to add user. Error: {e}"
            self._logger.error(err_msg)
            raise BadRequest(err_msg)
        else:
            self._logger.info(f"User {user} added!")