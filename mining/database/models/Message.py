"""
Entity model: Message
"""
from __future__ import annotations
from sqlalchemy.sql import func
from sqlalchemy import Index
from mining.database import db

class Message(db.Model):
    """
    Entity model: Message
    """
    __tablename__ = "Messages"

    MessageId = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    Thread_ThreadId = db.Column(db.Integer, db.ForeignKey("Threads.ThreadId"), nullable=False)
    User_UserId = db.Column(db.Integer, db.ForeignKey("Users.UserId"), nullable=False)
    LikeCount = db.Column(db.Integer, nullable=False)
    DislikeCount = db.Column(db.Integer, nullable=False)
    Message = db.Column(db.String, nullable=False)
    MessageNumber = db.Column(db.Integer, nullable=False)
    CreateDate = db.Column(db.BigInteger, nullable=False)
    LastUpdate = db.Column(db.BigInteger, nullable=False)
    RetrievedDate = \
        db.Column(db.DateTime, server_default=func.now(), nullable=False, onupdate=func.now())

    User = db.relation("User")

    __table_args__ = (Index("Messages_UserUserId_ThreadThreadId", "User_UserId", "Thread_ThreadId"),)

    def __repr__(self):
        return f"<Message(Thread_ThreadId={self.Thread_ThreadId}, " \
               f"MessageNumber={self.MessageNumber}, " \
               f"Message={self.Message[:20] if self.Message else ''})>"

    def Update(self, message: Message):
        '''
        Updates the object based on the given message.
        '''
        if self.LastUpdate > message.LastUpdate:
            return

        self.LikeCount = message.LikeCount if message.LikeCount is not None else self.LikeCount
        self.DislikeCount = message.DislikeCount if message.DislikeCount is not None else self.DislikeCount
        self.Message = message.Message if message.Message is not None else self.Message
        self.MessageNumber = message.MessageNumber if message.MessageNumber is not None else self.MessageNumber
        self.CreateDate = message.CreateDate if message.CreateDate is not None else self.CreateDate
        self.LastUpdate = message.LastUpdate if message.LastUpdate is not None else self.LastUpdate

    def Serialize(self):
        '''
        Returns a serialized representation of the object.
        '''
        return {
            "MessageId": self.MessageId,
            "Message": self.Message,
            "User": self.User.Serialize() if self.User is not None else None
        }

    def Copy(self):
        '''
        Returns a copy of the object.
        '''
        clone = Message(LastUpdate=self.LastUpdate - 1)
        clone.Update(self)

        clone.User = self.User.Copy() if self.User is not None else None
        return clone
