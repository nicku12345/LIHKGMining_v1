from __future__ import annotations
from mining.database import db
from sqlalchemy.sql import func

class Thread(db.Model):
    __tablename__ = "Threads"

    ThreadId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_UserId = db.Column(db.Integer, db.ForeignKey("Users.UserId"), nullable=False)
    LIHKGThreadId = db.Column(db.Integer, unique=True, nullable=False)
    CategoryId = db.Column(db.Integer, nullable=False)
    SubCategoryId = db.Column(db.Integer, nullable=False)
    Title = db.Column(db.String, nullable=False)
    NumberOfReplies = db.Column(db.Integer, nullable=False)
    NumberOfUniReplies = db.Column(db.Integer, nullable=False)
    LikeCount = db.Column(db.Integer, nullable=False)
    DislikeCount = db.Column(db.Integer, nullable=False)
    CreateDate = db.Column(db.BigInteger, nullable=False)
    LastUpdate = db.Column(db.BigInteger, nullable=False)
    RetrievedDate = db.Column(db.DateTime, server_default=func.now(), nullable=False, onupdate=func.now())

    User = db.relationship("User")
    Messages = db.relationship("Message")


    def Update(self, thread: Thread):
        if self.LastUpdate > thread.LastUpdate:
            return

        self.LIHKGThreadId = thread.LIHKGThreadId if thread.LIHKGThreadId!=None else self.LIHKGThreadId
        self.CategoryId = thread.CategoryId if thread.CategoryId!=None else self.CategoryId
        self.SubCategoryId = thread.SubCategoryId if thread.SubCategoryId!=None else self.SubCategoryId
        self.Title = thread.Title if thread.Title!=None else self.Title
        self.NumberOfReplies = thread.NumberOfReplies if thread.NumberOfReplies!=None else self.NumberOfReplies
        self.NumberOfUniReplies = thread.NumberOfUniReplies if thread.NumberOfUniReplies!=None else self.NumberOfUniReplies
        self.LikeCount = thread.LikeCount if thread.LikeCount!=None else self.LikeCount
        self.DislikeCount = thread.DislikeCount if thread.DislikeCount!=None else self.DislikeCount
        self.CreateDate = thread.CreateDate if thread.CreateDate!=None else self.CreateDate
        self.LastUpdate = thread.LastUpdate if thread.LastUpdate!=None else self.LastUpdate

    def __repr__(self):
        return f"<Thread(LIHKGThreadId={self.LIHKGThreadId}, " \
               f"Title={self.Title}, " \
               f"LikeCount={self.LikeCount}, " \
               f"DislikeCount={self.DislikeCount}, " \
               f"MessagesCount={len(self.Messages) if self.Messages!=None else 0}, " \
               f"User_UserId={self.User_UserId}>"

    def Serialize(self):
        return {
            "LIHKGThreadId": self.LIHKGThreadId,
            "CategoryId": self.CategoryId,
            "SubCategoryId": self.SubCategoryId,
            "NumberOfReplies": self.NumberOfReplies,
            "NumberOfUniReplies": self.NumberOfUniReplies,
            "LikeCount": self.LikeCount,
            "DislikeCount": self.DislikeCount,
            "User": self.User.Serialize() if self.User!=None else None,
            "Messages": [msg.Serialize() for msg in self.Messages if msg!=None],
            "CreateDate": self.CreateDate,
            "LastUpdate": self.LastUpdate,
        }

    def Copy(self):
        clone = Thread(LastUpdate=self.LastUpdate - 1)
        clone.Update(self)

        clone.Messages = [msg.Copy() for msg in self.Messages if msg!=None]
        clone.User = self.User.Copy() if self.User!=None else None
        return clone
