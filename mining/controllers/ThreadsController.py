"""
Controller for thread entities related functionalities
"""
import json
from flask import Blueprint, Response
from mining.managers.ThreadsManager import ThreadsManager


class ThreadsController:
    """
    Controller for thread entities related functionalities
    """

    blueprint = Blueprint("threads", __name__, url_prefix="/api/threads")

    @staticmethod
    @blueprint.route("/query/all", methods=["GET"])
    def QueryAllThreads():
        '''
        Query all the threads in stored in the database.
        '''
        threadsManager = ThreadsManager()

        allThreads = threadsManager.QueryAllThreads(skip_messages=True)
        res = [thread.Serialize() for thread in allThreads]

        return Response(json.dumps(res), mimetype="application/json")
