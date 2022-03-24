"""
The appsettings class. Stores configurations for the application.
"""
import logging
import coloredlogs
from flask import Flask
from dataclasses import dataclass

@dataclass
class Appsettings:
    """
    The appsettings class. Stores configurations for the application.
    """

    SQLALCHEMY_DATABASE_URI         : str
    SQLALCHEMY_TRACK_MODIFICATIONS  : bool
    LOG_PATH                        : str = "./mining/data/logs/flask.log"
    IS_TEST                         : bool = False
    ENVIRONMENT                     : str = "DEV"

    def ApplySettings(self, app: Flask):
        '''
        Apply the appsettings_env.py to the Flask app instance.
        '''

        '''
        BASE SETTINGS and SQLALCHEMY SETTINGS
        '''
        app.config["SQLALCHEMY_DATABASE_URI"] = self.SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = self.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config["IS_TEST"] = self.IS_TEST


        '''
        LOGGING SETTINGS

        Get rid of the default logger and apply customized logging format.
        See https://stackoverflow.com/questions/14888799/disable-console-messages-in-flask-server
        '''
        coloredlogs.install()
        app.logger.handlers.clear()
        logging.getLogger("werkzeug").handlers.clear()

        logging.basicConfig(
            format='[%(asctime)s] %(levelname)s: \t%(message)s',
            level=logging.DEBUG,
        )
