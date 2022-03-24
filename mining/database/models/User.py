"""
Entity model of a user.
"""
from __future__ import annotations
from sqlalchemy.sql import func
from sqlalchemy import Index
from mining.database import db

class User(db.Model):
    """
    Entity model of a user.
    """
    __tablename__ = "Users"

    UserId = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    LIHKGUserId = db.Column(db.Integer, unique=True, nullable=False)
    Nickname = db.Column(db.String, nullable=False)
    Gender = db.Column(db.String(1), nullable=False)
    CreateDate = db.Column(db.BigInteger, nullable=False)
    LastUpdate = db.Column(db.BigInteger, nullable=False)
    RetrievedDate = db.Column(db.DateTime, server_default=func.now(), nullable=False, onupdate=func.now())

    __table_args__ = (Index("Users_UserId_LIHKGUserId", "UserId", "LIHKGUserId"),)

    def __repr__(self):
        '''
        Returns a representation of self.
        '''
        return f"<User(LIHKGUserId={self.LIHKGUserId}, " \
               f"Nickname={self.Nickname}, " \
               f"Gender={self.Gender}, " \
               f"CreateDate={self.CreateDate}, " \
               f"LastUpdate={self.LastUpdate}, " \
               f"RetrievedDate={self.RetrievedDate})>"

    def Update(self, user: User):
        '''
        Updates self based on the given user.
        '''
        if self.LastUpdate is None or self.LastUpdate > user.LastUpdate:
            return

        self.LIHKGUserId = user.LIHKGUserId if user.LIHKGUserId is not None else self.LIHKGUserId
        self.Nickname = user.Nickname if user.Nickname is not None else self.Nickname
        self.Gender = user.Gender if user.Gender is not None else self.Gender
        self.CreateDate = user.CreateDate if user.CreateDate is not None else self.CreateDate
        self.LastUpdate = user.LastUpdate if user.LastUpdate is not None else self.LastUpdate

    def Serialize(self):
        '''
        Returns a serialized representation of self.
        '''
        return {
            "LIHKGUserId": self.LIHKGUserId,
            "Nickname": self.Nickname,
            "Gender": self.Gender,
            "CreateDate": self.CreateDate,
            "LastUpdate": self.LastUpdate,
        }

    def Copy(self):
        '''
        Creates a copy of self.
        '''
        clone = User(LastUpdate=self.LastUpdate - 1)
        clone.Update(self)
        return clone
