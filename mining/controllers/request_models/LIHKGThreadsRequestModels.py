"""
Request models for LIHKG threads controller.
"""
from dataclasses import dataclass
from mining.util.Exceptions import BadRequest

@dataclass
class FullFetchThreadRequest:
    """
    Request model for full fetch thread.
    """
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
        '''
        Maps the request body into the request model.
        '''

        try:
            req = FullFetchThreadRequest(**body)
        except Exception as e:
            raise BadRequest(f"Mapping to FullFetchThreadRequest failed. Error: {e}") from e

        if not req.IsValid():
            raise BadRequest("Some required fields are None.") from None

        return req


@dataclass()
class FetchOneThreadPageRequest:
    """
    Request model for fetch one thread page.
    """
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
    def ConvertFromRequestBody(cls, body):
        '''
        Maps the request body into a request model.
        '''
        try:
            req = FetchOneThreadPageRequest(**body)
        except Exception as e:
            raise BadRequest(f"Mapping to FetchOneThreadPageRequest failed. Error: {e}") from e

        if not req.IsValid():
            raise BadRequest("Some required fields are None.") from None

        return req
