"""
Request models for LIHKG users controller
"""
from dataclasses import dataclass
from mining.util.Exceptions import *

@dataclass
class QueryAllMessageByLIHKGUserIdRequest:
    """
    Request model for query all messages by LIHKGUserId
    """
    LIHKGUserId: int

    def IsValid(self):
        '''
        Check whether the types of the attributes are as desired
        '''

        if not isinstance(self.LIHKGUserId, int):
            return False
        return True

    @classmethod
    def ConvertFromRequestBody(cls, body):
        '''
        Maps the request body into the request model
        '''

        try:
            req = QueryAllMessageByLIHKGUserIdRequest(**body)
        except Exception as e:
            raise BadRequest(f"Mapping to QueryAllMessageByLIHKGUserIdRequest failed. Error: {e}") from e

        if not req.IsValid():
            raise BadRequest(f"Some required fields are None") from None

        return req
