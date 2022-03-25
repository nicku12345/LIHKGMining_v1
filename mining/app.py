"""
The LIHKGMiningApp class
"""
import random
from flask import Flask

class LIHKGMiningApp:
    """
    The LIHKGMiningApp class
    """

    @classmethod
    def CreateApp(cls, ENV="DEV"):
        '''
        Creates the main app based on the given env.
        '''
        app = Flask(__name__)

        if ENV == "DEV":
            from mining.config.appsettings_dev import APPSETTINGS
            app.run()
        elif ENV == "TEST":
            from mining.config.appsettings_test import APPSETTINGS
        elif ENV == "PROD":
            from mining.config.appsettings_prod import APPSETTINGS
        else:
            raise f"{ENV} is not a valid environment" from None

        APPSETTINGS.ApplySettings(app)

        from mining.database import DatabaseInitApp
        from mining.background_workers import BackgroundWorkersInitApp
        from mining.managers import ManagersInitApp
        from mining.controllers import ControllersInitApp

        DatabaseInitApp(app)
        ControllersInitApp(app)
        ManagersInitApp(app)
        BackgroundWorkersInitApp(app)

        app.run(port=5000 + random.randint(0,999))

        return app
