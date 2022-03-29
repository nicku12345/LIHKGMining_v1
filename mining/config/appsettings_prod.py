"""
The appsettings for prod env
"""
from mining.config.base_appsettings import Appsettings
from mining.config.database_secrets.ConnectionStrings import PROD_CONNECTION_STRING

APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI=PROD_CONNECTION_STRING,
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)
