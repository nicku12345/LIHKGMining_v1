
from flask import Flask
import logging
import coloredlogs

class Appsettings:

    def __init__(self, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, IS_TEST=False):
        self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
        self.SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS
        self.IS_TEST = IS_TEST

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
            level=logging.DEBUG
        )