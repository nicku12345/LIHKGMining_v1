from mining.util.Exceptions import *


class FullFetchThreadRequest:

    def __init__(self, LIHKGThreadId: int, page: int = 1):
        self.LIHKGThreadId = LIHKGThreadId
        self.page = page

    def IsValid(self):
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


class FetchOneThreadPageRequest:

    def __init__(self, LIHKGThreadId: int, page: int):
        self.LIHKGThreadId = LIHKGThreadId
        self.page = page

    def IsValid(self):
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