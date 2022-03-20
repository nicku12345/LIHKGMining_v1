from __future__ import annotations
from mining.database import db
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = "Users"

    UserId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    LIHKGUserId = db.Column(db.Integer, unique=True, nullable=False)
    Nickname = db.Column(db.String, nullable=False)
    Gender = db.Column(db.String, nullable=False)
    CreateDate = db.Column(db.BigInteger, nullable=False)
    LastUpdate = db.Column(db.BigInteger, nullable=False)
    RetrievedDate = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<User(LIHKGUserId={self.LIHKGUserId}, " \
               f"Nickname={self.Nickname}, " \
               f"Gender={self.Gender}, " \
               f"CreateDate={self.CreateDate}, " \
               f"LastUpdate={self.LastUpdate}, " \
               f"RetrievedDate={self.RetrievedDate})>"

    def Update(self, user: User):
        if self.LastUpdate == None or self.LastUpdate > user.LastUpdate:
            return

        self.LIHKGUserId = user.LIHKGUserId if user.LIHKGUserId!=None else self.LIHKGUserId
        self.Nickname = user.Nickname if user.Nickname!=None else self.Nickname
        self.Gender = user.Gender if user.Gender!=None else self.Gender
        self.CreateDate = user.CreateDate if user.CreateDate!=None else self.CreateDate
        self.LastUpdate = user.LastUpdate if user.LastUpdate!=None else self.LastUpdate
        self.RetrievedDate = user.RetrievedDate if user.RetrievedDate!=None else func.now()

    def Serialize(self):
        return {
            "LIHKGUserId": self.LIHKGUserId,
            "Nickname": self.Nickname,
            "Gender": self.Gender,
            "CreateDate": self.CreateDate,
            "LastUpdate": self.LastUpdate,
        }

    def Copy(self):
        clone = User(LastUpdate=self.LastUpdate - 1)
        clone.Update(self)
        return clone
