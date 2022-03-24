"""
Do necessary init for the controllers.
"""
from mining.controllers.misc.HelloWorldController import HelloWorldController
from mining.controllers.LIHKGThreadsController import LIHKGThreadsController

def ControllersInitApp(app):
    """
    Do necessary init for the controllers.
    """
    app.register_blueprint(HelloWorldController.blueprint)
    app.register_blueprint(LIHKGThreadsController.blueprint)
