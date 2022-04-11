"""
Controller for LIHKG users related functionalities
"""
import json

from flask import Blueprint, request, Response
from mining.managers.UsersManager import UsersManager
from mining.controllers.request_models.LIHKGUsersRequestModels import *


class LIHKGUsersController:
    """
    Controller for LIHKG users related functionalities
    """

    blueprint = Blueprint("lihkgusers", __name__, url_prefix="/api/lihkgusers")

    @staticmethod
    @blueprint.route("/messages/query/all", methods=["POST"])
    def QueryAllMessagesByLIHKGThreads():
        '''
        Query all messages for a specific LIHKG User id
        :return:
        '''

        body = request.json
        requestModel = QueryAllMessageByLIHKGUserIdRequest.ConvertFromRequestBody(body)

        userMgr = UsersManager()
        msgThreads_pairs = userMgr.QueryAllMessagesFromUserByLIHKGUserId(requestModel.LIHKGUserId)

        # representation of json response
        res = [{"Message": msg.Serialize(), "Thread": t.Serialize()} for msg,t in msgThreads_pairs]

        return Response(json.dumps(res), mimetype="application/json")
