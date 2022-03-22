from flask import Blueprint

class HelloWorldController:
    '''
    This controller is for testing purpose
    '''

    blueprint = Blueprint("/", __name__)

    @staticmethod
    @blueprint.route("/")
    def HelloWorld():
        return "Hello world!"