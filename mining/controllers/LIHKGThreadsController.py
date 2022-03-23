from flask import Blueprint, request
from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager
from mining.controllers.requestModels.LIHKGThreadsRequestModels import *

from mining.background_workers.WorkQueue import LIHKGThreadsWORKQUEUE


class LIHKGThreadsController:

    blueprint = Blueprint("lihkgthreads", __name__, url_prefix="/api/lihkgthreads")

    @staticmethod
    @blueprint.route("/fetch", methods=["POST"])
    def FetchOneThreadPageByLIHKGThreadIdAndPage():
        body = request.json
        requestModel = FetchOneThreadPageRequest.ConvertFromRequestBody(body)
        lihkgThreadsManager = LIHKGThreadsManager()
        lihkgThreadsManager.FetchOneThreadPageByLIHKGThreadId(requestModel.LIHKGThreadId, requestModel.page)
        return "ok"

    @staticmethod
    @blueprint.route("/fullfetch", methods=["POST"])
    def FullFetchOneThreadByLIHKGThreadId():
        body = request.json
        requestModel = FullFetchThreadRequest.ConvertFromRequestBody(body)

        lihkgThreadsManager = LIHKGThreadsManager()
        lihkgThreadsManager.FullFetchOneThreadByLIHKGThreadIdWithRetry(requestModel.LIHKGThreadId, requestModel.page)

        return "ok"

    @staticmethod
    @blueprint.route("/fullfetch/queue", methods=["POST"])
    def QueueFullFetchOneThreadByLIHKGThreadId():
        body = request.json
        requestModel = FullFetchThreadRequest.ConvertFromRequestBody(body)
        LIHKGThreadsWORKQUEUE.Put(requestModel.LIHKGThreadId, requestModel.page, True)

        return "ok"

    @staticmethod
    @blueprint.route("/fetch/queue", methods=["POST"])
    def QueueFetchOneThreadPageByLIHKGThreadIdAndPage():
        body = request.json
        requestModel = FetchOneThreadPageRequest.ConvertFromRequestBody(body)
        LIHKGThreadsWORKQUEUE.Put(requestModel.LIHKGThreadId, requestModel.page, False)

        return "ok"