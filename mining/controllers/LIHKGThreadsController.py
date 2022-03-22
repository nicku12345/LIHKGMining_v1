from flask import Blueprint, request
from mining.managers.LIHKGThreadsManager import LIHKGThreadsManager
from mining.controllers.requestModels.LIHKGThreadsRequestModels import *


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
        lihkgThreadsManager.FullFetchOneThreadByLIHKGThreadId(requestModel.LIHKGThreadId, requestModel.page)
        return "ok"