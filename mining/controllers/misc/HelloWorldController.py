"""
Controller for testing purpose
"""
from flask import Blueprint

class HelloWorldController:
    '''
    This controller is for testing purpose
    '''

    blueprint = Blueprint("/", __name__)

    @staticmethod
    @blueprint.route("/")
    def HelloWorld():
        '''
        A testing route for checking whether server is live
        '''
        return "Hello world!"
