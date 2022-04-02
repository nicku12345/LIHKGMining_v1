"""
Concrete class of describing a LIHKG thread job.
"""
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class LIHKGThreadsJob:
    '''
    A job class indicating a specification for a LIHKG thread fetch job.
    '''

    LIHKGThreadId   : int
    page            : int
    isFullFetch     : bool
    CreateTime      : datetime = field(default_factory=datetime.utcnow)

    def Serialize(self):
        '''
        Serialize self.
        '''
        return {
            "LIHKGThreadId": self.LIHKGThreadId,
            "page": self.page,
            "isFullFetch": self.isFullFetch,
            "CreateTime": str(self.CreateTime)
        }
