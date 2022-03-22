from typing import List
from mining.database.repositories.BaseRepository import BaseRepository
from mining.database.models.User import User

class UsersRepository(BaseRepository):

    def QueryAllUsers(self):
        '''
        Return a list of all existing users in the attached Users table

        '''
        return self._db.session.query(User).all()

    def QueryUserByLIHKGUserId(self, LIHKGUserId: int):
        '''
        Return a user having the queried LIHKGUserId.

        Return None otherwise.
        '''
        return self._db.session.query(User).filter_by(LIHKGUserId = LIHKGUserId).first()

    def QueryUsersByLIHKGUserIds(self, LIHKGUserIds: List[int]):
        LIHKGUserId_UserMap = dict()
        users = self._db.session.query(User).filter(User.LIHKGUserId.in_(LIHKGUserIds)).all()

        for u in users:
            LIHKGUserId_UserMap[u.LIHKGUserId] = u

        return LIHKGUserId_UserMap

    def AddUser(self, user: User):
        '''
        Calls the SQLAlchemy db.session.add method and commits the changes
        '''
        self.AddAndSave(user)

    def MergeUser(self, user: User):
        '''
        Calls the SQLAlchemy db.session.merge method and commits the changes
        '''
        self.MergeAndSave(user)