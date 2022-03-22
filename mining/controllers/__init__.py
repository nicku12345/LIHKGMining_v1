from mining.controllers.misc.HelloWorldController import HelloWorldController
from mining.controllers.LIHKGThreadsController import LIHKGThreadsController

def ControllersInitApp(app):
    app.register_blueprint(HelloWorldController.blueprint)
    app.register_blueprint(LIHKGThreadsController.blueprint)