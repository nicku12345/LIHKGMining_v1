"""
Mock data for messages.
"""
from mining.database.models.Message import Message

mock_messages = [
    Message(MessageId=1, Thread_ThreadId=1, User_UserId=1, LikeCount=0, DislikeCount=0, Message="test message", MessageNumber=0, CreateDate=82, LastUpdate=90),
    Message(MessageId=2, Thread_ThreadId=1, User_UserId=2, LikeCount=0, DislikeCount=1, Message="test reply", MessageNumber=1, CreateDate=180, LastUpdate=200)
]
