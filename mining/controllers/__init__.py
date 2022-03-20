from mining.controllers.misc.HelloWorldController import HelloWorldController

def ControllersInitApp(app):
    app.register_blueprint(HelloWorldController.blueprint)