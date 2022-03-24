"""
Entity model of a thread.
"""
from __future__ import annotations
from sqlalchemy.sql import func
from mining.database import db

class Thread(db.Model):
    """
    Entity model of a thread.
    """
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
        '''
        Updates self based on the given thread.
        '''
        if self.LastUpdate > thread.LastUpdate:
            return

        self.LIHKGThreadId = thread.LIHKGThreadId if thread.LIHKGThreadId is not None else self.LIHKGThreadId
        self.CategoryId = thread.CategoryId if thread.CategoryId is not None else self.CategoryId
        self.SubCategoryId = thread.SubCategoryId if thread.SubCategoryId is not None else self.SubCategoryId
        self.Title = thread.Title if thread.Title is not None else self.Title
        self.NumberOfReplies = thread.NumberOfReplies if thread.NumberOfReplies is not None else self.NumberOfReplies
        self.NumberOfUniReplies = thread.NumberOfUniReplies if thread.NumberOfUniReplies is not None else self.NumberOfUniReplies
        self.LikeCount = thread.LikeCount if thread.LikeCount is not None else self.LikeCount
        self.DislikeCount = thread.DislikeCount if thread.DislikeCount is not None else self.DislikeCount
        self.CreateDate = thread.CreateDate if thread.CreateDate is not None else self.CreateDate
        self.LastUpdate = thread.LastUpdate if thread.LastUpdate is not None else self.LastUpdate

    def __repr__(self):
        '''
        Returns a representation of self
        '''
        return f"<Thread(LIHKGThreadId={self.LIHKGThreadId}, " \
               f"Title={self.Title}, " \
               f"LikeCount={self.LikeCount}, " \
               f"DislikeCount={self.DislikeCount}, " \
               f"MessagesCount={len(self.Messages) if self.Messages is not None else 0}, " \
               f"User_UserId={self.User_UserId}>"

    def Serialize(self):
        '''
        Returns a serialized representation of self.
        '''
        return {
            "LIHKGThreadId": self.LIHKGThreadId,
            "CategoryId": self.CategoryId,
            "SubCategoryId": self.SubCategoryId,
            "NumberOfReplies": self.NumberOfReplies,
            "NumberOfUniReplies": self.NumberOfUniReplies,
            "LikeCount": self.LikeCount,
            "DislikeCount": self.DislikeCount,
            "User": self.User.Serialize() if self.User!=None else None,
            "Messages": [msg.Serialize() for msg in self.Messages if msg is not None],
            "CreateDate": self.CreateDate,
            "LastUpdate": self.LastUpdate,
        }

    def Copy(self):
        '''
        Creates a copy of self
        '''
        clone = Thread(LastUpdate=self.LastUpdate - 1)
        clone.Update(self)

        clone.Messages = [msg.Copy() for msg in self.Messages if msg is not None]
        clone.User = self.User.Copy() if self.User is not None else None
        return clone
