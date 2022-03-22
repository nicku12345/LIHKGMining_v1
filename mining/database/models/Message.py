from __future__ import annotations
from mining.database import db
from sqlalchemy.sql import func

class Message(db.Model):
    __tablename__ = "Messages"

    MessageId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Thread_ThreadId = db.Column(db.Integer, db.ForeignKey("Threads.ThreadId"), nullable=False)
    User_UserId = db.Column(db.Integer, db.ForeignKey("Users.UserId"), nullable=False)
    LikeCount = db.Column(db.Integer, nullable=False)
    DislikeCount = db.Column(db.Integer, nullable=False)
    Message = db.Column(db.String, nullable=False)
    MessageNumber = db.Column(db.Integer, nullable=False)
    CreateDate = db.Column(db.BigInteger, nullable=False)
    LastUpdate = db.Column(db.BigInteger, nullable=False)
    RetrievedDate = db.Column(db.DateTime, server_default=func.now(), nullable=False, onupdate=func.now())

    User = db.relation("User")

    def __repr__(self):
        return f"<Message(Thread_ThreadId={self.Thread_ThreadId}, MessageNumber={self.MessageNumber}, Message={self.Message[:20] if self.Message else ''})>"

    def Update(self, message: Message):
        if self.LastUpdate > message.LastUpdate:
            return

        self.LikeCount = message.LikeCount if message.LikeCount!=None else self.LikeCount
        self.DislikeCount = message.DislikeCount if message.DislikeCount!=None else self.DislikeCount
        self.Message = message.Message if message.Message!=None else self.Message
        self.MessageNumber = message.MessageNumber if message.MessageNumber!=None else self.MessageNumber
        self.CreateDate = message.CreateDate if message.CreateDate!=None else self.CreateDate
        self.LastUpdate = message.LastUpdate if message.LastUpdate!=None else self.LastUpdate

    def Serialize(self):
        return {
            "MessageId": self.MessageId,
            "Message": self.Message,
            "User": self.User.Serialize() if self.User!=None else None
        }

    def Copy(self):
        clone = Message(LastUpdate=self.LastUpdate - 1)
        clone.Update(self)

        clone.User = self.User.Copy() if self.User!=None else None
        return clone

