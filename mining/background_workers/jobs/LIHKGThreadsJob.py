"""
Concrete class of describing a LIHKG thread job.
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LIHKGThreadsJob:
    '''
    A job class indicating a specification for a LIHKG thread fetch job.
    '''

    LIHKGThreadId   : int
    page            : int
    isFullFetch     : bool
    CreateTime      : datetime = datetime.utcnow()
