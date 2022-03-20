
from flask import Flask
import logging

class Appsettings:

    def __init__(self, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, IS_TEST=False):
        self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
        self.SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS
        self.IS_TEST = IS_TEST

    def ApplySettings(self, app: Flask):
        app.config["SQLALCHEMY_DATABASE_URI"] = self.SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = self.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config["IS_TEST"] = self.IS_TEST

        app.logger.handlers.clear()
        logging.basicConfig(format='[%(asctime)s - %(levelname)s] %(message)s', level=logging.DEBUG)