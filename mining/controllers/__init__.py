"""
Do necessary init for the controllers.
"""
from mining.controllers.misc.HelloWorldController import HelloWorldController
from mining.controllers.LIHKGThreadsController import LIHKGThreadsController
from mining.controllers.LIHKGUsersController import LIHKGUsersController
from mining.controllers.ThreadsController import ThreadsController

def ControllersInitApp(app):
    """
    Do necessary init for the controllers.
    """
    app.register_blueprint(HelloWorldController.blueprint)
    app.register_blueprint(LIHKGThreadsController.blueprint)
    app.register_blueprint(LIHKGUsersController.blueprint)
    app.register_blueprint(ThreadsController.blueprint)
