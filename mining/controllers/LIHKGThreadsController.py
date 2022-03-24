"""
Controller for LIHKG threads related functionalities
"""
from flask import Blueprint, request
from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager
from mining.controllers.request_models.LIHKGThreadsRequestModels import *

from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob
from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE


class LIHKGThreadsController:
    """
    Controller for LIHKG threads related functionalities
    """

    blueprint = Blueprint("lihkgthreads", __name__, url_prefix="/api/lihkgthreads")

    @staticmethod
    @blueprint.route("/fetch", methods=["POST"])
    def FetchOneThreadPageByLIHKGThreadIdAndPage():
        '''
        Sends a request to fetch one LIHKG thread page by the specified LIHKGThreadId and page.

        The task is performed synchronously and returns "ok" to the client once fetched.

        This API should be for testing purpose only.

        Example request body: (Case-sensitive)
        {
            "LIHKGThreadId": 123,
            "page": 1
        }
        '''
        body = request.json
        requestModel = FetchOneThreadPageRequest.ConvertFromRequestBody(body)

        lihkgThreadsManager = LIHKGThreadsManager()
        lihkgThreadsManager.FetchOneThreadPageByLIHKGThreadId(
            requestModel.LIHKGThreadId,
            requestModel.page
        )
        return "ok"

    @staticmethod
    @blueprint.route("/fetch/queue", methods=["POST"])
    def QueueFetchOneThreadPageByLIHKGThreadIdAndPage():
        '''
        Sends a request to fetch one LIHKG thread page by the specified LIHKGThreadId and page.

        The task is queued to a global work queue and will be processed asynchronously.

        Returns "ok" to the client once the task is successfully queued.

        Example request body: (Case-sensitive)
        {
            "LIHKGThreadId": 123,
            "page": 1
        }
        '''
        body = request.json
        requestModel = FetchOneThreadPageRequest.ConvertFromRequestBody(body)

        job = LIHKGThreadsJob(
            LIHKGThreadId=requestModel.LIHKGThreadId,
            page=requestModel.page,
            isFullFetch=False
        )

        LIHKGThreadsWORKQUEUE.Put(job)

        return "ok"

    @staticmethod
    @blueprint.route("/fullfetch", methods=["POST"])
    def FullFetchOneThreadByLIHKGThreadId():
        '''
        Sends a request to fetch one LIHKG thread, starting
        from the specified starting page to the end of the thread.

        The task is performed synchronously and returns "ok" to the client once fetched.

        This API is not recommended. Please use the "/fullfetch/queue" API instead.

        Example request body: (Case-sensitive)
        {
            "LIHKGThreadId": 123,
            "page": 10              // page parameter is optional
        }
        '''
        body = request.json
        requestModel = FullFetchThreadRequest.ConvertFromRequestBody(body)

        lihkgThreadsManager = LIHKGThreadsManager()
        lihkgThreadsManager.FullFetchOneThreadByLIHKGThreadIdWithRetry(
            requestModel.LIHKGThreadId,
            requestModel.page
        )

        return "ok"

    @staticmethod
    @blueprint.route("/fullfetch/queue", methods=["POST"])
    def QueueFullFetchOneThreadByLIHKGThreadId():
        '''
        Sends a request to fetch one LIHKG thread, starting
        from the specified starting page to the end of the thread.

        The task is queued to a global work queue and will be processed asynchronously.

        Returns "ok" to the client once the task is successfully queued.

        Example request body: (Case-sensitive)
        {
            "LIHKGThreadId": 123,
            "page": 10              // page parameter is optional
        }
        '''
        body = request.json
        requestModel = FullFetchThreadRequest.ConvertFromRequestBody(body)

        job = LIHKGThreadsJob(
            LIHKGThreadId=requestModel.LIHKGThreadId,
            page=requestModel.page,
            isFullFetch=True
        )

        LIHKGThreadsWORKQUEUE.Put(job)

        return "ok"
