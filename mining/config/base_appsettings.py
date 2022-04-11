"""
The appsettings class. Stores configurations for the application.
"""
import logging
from dataclasses import dataclass
from logging.handlers import TimedRotatingFileHandler
import coloredlogs
from flask import Flask
from mining.config.options.LIHKGThreadsManagerOptions import LIHKGThreadsManagerOptions
from mining.config.options.PlaywrightHelperOptions import PlaywrightHelperOptions
from mining.config.options.LIHKGThreadsWorkerOptions import LIHKGThreadsWorkerOptions
from mining.config.options.BaseWorkerOptions import BaseWorkerOptions


@dataclass
class Appsettings:
    """
    The appsettings class. Stores configurations for the application.
    """

    # General settings
    SQLALCHEMY_DATABASE_URI         : str
    SQLALCHEMY_TRACK_MODIFICATIONS  : bool
    SQLALCHEMY_ECHO                 : bool = False
    LOG_PATH                        : str = "./mining/data/logs/flask.log"
    IS_TEST                         : bool = False
    ENVIRONMENT                     : str = "DEV"

    # Settings on LIHKGThreadsManager
    LIHKGThreadsManagerOptions      : LIHKGThreadsManagerOptions = None

    # Settings on PlaywrightHelper
    PlaywrightHelperOptions         : PlaywrightHelperOptions = None

    # Settings on LIHKGThreadsWorker
    LIHKGThreadsWorkerOptions       : LIHKGThreadsWorkerOptions = None

    # Settings on BaseWorker
    BaseWorkerOptions               : BaseWorkerOptions = None

    def ApplySettings(self, app: Flask):
        '''
        Apply the appsettings_env.py to the Flask app instance.
        '''

        '''
        BASE SETTINGS and SQLALCHEMY SETTINGS
        '''
        app.config["SQLALCHEMY_DATABASE_URI"] = self.SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = self.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config["SQLALCHEMY_ECHO"] = self.SQLALCHEMY_ECHO
        app.config["IS_TEST"] = self.IS_TEST
        app.config["ENVIRONMENT"] = self.ENVIRONMENT

        '''
        LOGGING SETTINGS

        Get rid of the default logger and apply customized logging format.
        See https://stackoverflow.com/questions/14888799/disable-console-messages-in-flask-server
        '''
        self.ApplyLoggingSettings(app)

    def ApplyLoggingSettings(self, app):
        '''
        Apply the logging settings to the app.

        It mainly manages the werkzeug (the default logger from the framework)
        and the flask app logger.
        '''
        app.logger.handlers.clear()

        # Werkzeug logger settings
        werkzeug_logger = logging.getLogger("werkzeug")
        werkzeug_logger.handlers.clear()

        # flask app logger settings
        flask_app_logger = logging.getLogger("flask.app")
        flask_app_logger.handlers.clear()

        # common stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        # formatter of the stream handler
        flask_app_formatter = logging.Formatter('[%(asctime)s] %(levelname)s: \t%(message)s')

        # apply the formatter to all handlers
        stream_handler.setFormatter(flask_app_formatter)

        flask_app_logger.addHandler(stream_handler)
        # add this handler only if it is not test
        werkzeug_logger.addHandler(stream_handler)

        coloredlogs.install(logger=flask_app_logger, level=logging.DEBUG)
        coloredlogs.install(logger=werkzeug_logger, level=logging.DEBUG)
