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

    def AddUser(self, user: User):
        self._logger.info(f"Adding user...")
        self._logger.debug(user)
        try:
            self._usersRepo.AddUser(user)
        except Exception as e:
            self._logger.error(f"Failed to add user. Error: {e}")
            raise BadRequest(f"Failed add {user}. Error: {e}")
        else:
            self._logger.info("User added!")