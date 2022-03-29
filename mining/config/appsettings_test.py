"""
The appsettings for test env
"""
from mining.config.base_appsettings import Appsettings
from mining.config.database_secrets.ConnectionStrings import TEST_CONNECTION_STRING

APPSETTINGS = Appsettings(
    SQLALCHEMY_DATABASE_URI=TEST_CONNECTION_STRING,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    IS_TEST=True
)
