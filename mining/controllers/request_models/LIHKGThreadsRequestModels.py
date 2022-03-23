from dataclasses import dataclass
from mining.util.Exceptions import *

@dataclass
class FullFetchThreadRequest:
    LIHKGThreadId   : int
    page            : int = 1

    def IsValid(self):
        '''
        Check whether the types of the attributes are as desired.
        '''

        if not isinstance(self.LIHKGThreadId, int):
            return False
        if not isinstance(self.page, int):
            return False
        return True

    @classmethod
    def ConvertFromRequestBody(cls, body):
        try:
            req = FullFetchThreadRequest(**body)
        except Exception as e:
            raise BadRequest(f"Mapping to FullFetchThreadRequest failed. Error: {e}")

        if not req.IsValid():
            raise BadRequest(f"Some required fields are None.")

        return req


@dataclass()
class FetchOneThreadPageRequest:
    LIHKGThreadId   : int
    page            : int

    def IsValid(self):
        '''
        Check whether the types of the attributes are as desired.
        '''

        if not isinstance(self.LIHKGThreadId, int):
            return False
        if not isinstance(self.page, int):
            return False
        return True

    @classmethod
    def ConvertFromRequestBody(self, body):
        try:
            req = FetchOneThreadPageRequest(**body)
        except Exception as e:
            raise BadRequest(f"Mapping to FetchOneThreadPageRequest failed. Error: {e}")

        if not req.IsValid():
            raise BadRequest(f"Some required fields are None.")

        return req