"""
Controller for LIHKG threads related functionalities
"""
import json
from flask import Blueprint, request, Response
from mining.controllers.request_models.LIHKGThreadsRequestModels import *
from mining.background_workers.jobs.LIHKGThreadsJob import LIHKGThreadsJob
from mining.background_workers.LIHKGThreadsWorkQueue import LIHKGThreadsWORKQUEUE


class LIHKGThreadsController:
    """
    Controller for LIHKG threads related functionalities
    """

    blueprint = Blueprint("lihkgthreads", __name__, url_prefix="/api/lihkgthreads")

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

    @staticmethod
    @blueprint.route("/queue", methods=["GET"])
    def GetLIHKGThreadsWorkQueue():
        '''
        Query all the work in the LIHKG threads work queue.
        '''
        jobs = LIHKGThreadsWORKQUEUE.QueryAllWork()
        res = [job.Serialize() for job in jobs]
        return Response(json.dumps(res), mimetype="application/json")

    @staticmethod
    @blueprint.route("/queue/clear", methods=["POST"])
    def ClearLIHKGThreadsWorkQueue():
        '''
        Clear the LIHKG threads work queue.
        '''
        LIHKGThreadsWORKQUEUE.ClearAllWork()
        return "ok"
