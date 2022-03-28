"""
The appsettings class. Stores configurations for the application.
"""
import logging
from dataclasses import dataclass
from logging.handlers import TimedRotatingFileHandler
import coloredlogs
from flask import Flask

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

    # If set true, LIHKG thread worker will automatically fetch for jobs
    IS_AUTO_FETCH_LIHKGTHREADJOBS   : bool = False

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
        app.config["ENVIRONMENT"] = self.ENVIRONMENT
        app.config["IS_AUTO_FETCH_LIHKGTHREADJOBS"] = self.IS_AUTO_FETCH_LIHKGTHREADJOBS

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

        # Save log to files only if it is not a test environment
        if not self.IS_TEST:
            # common file handler
            file_handler = TimedRotatingFileHandler(self.LOG_PATH, when="midnight", interval=1, encoding="utf8")

            file_handler.setLevel(logging.DEBUG)
            file_handler.suffix = "%Y%m%d"

            file_handler.setFormatter(flask_app_formatter)

            flask_app_logger.addHandler(file_handler)

        coloredlogs.install(logger=flask_app_logger, level=logging.DEBUG)
        coloredlogs.install(logger=werkzeug_logger, level=logging.DEBUG)
