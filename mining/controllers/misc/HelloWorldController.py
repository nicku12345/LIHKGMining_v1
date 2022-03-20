from flask import Blueprint

class HelloWorldController:

    blueprint = Blueprint("/", __name__)

    @staticmethod
    @blueprint.route("/")
    def HelloWorld():
        return "Hello world!"